"""
The web app: the page in public/ and the API route it calls, which holds your key.

Run it locally with `python app.py`, then open http://localhost:3000
On Vercel, this file becomes a Python function and public/ is served from the CDN.
"""
import os
import re
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from apiverve import ApiError, api_key, call_api, rate_limited

app = Flask(__name__)
PUBLIC = Path(__file__).with_name('public')


@app.before_request
def guard():
    """Every /api route needs the key, and counts against the visitor's rate limit."""
    if not request.path.startswith('/api/'):
        return None
    api_key()
    ip = request.headers.get('x-forwarded-for', '').split(',')[0].strip() or request.remote_addr or 'local'
    if rate_limited(ip):
        return fail('Too many requests. Wait a minute and try again.', 429)
    return None


@app.errorhandler(ApiError)
def api_error(err):
    return fail(str(err), err.status)


def fail(message, status=400):
    return jsonify(error=message), status

CURRENCY = re.compile(r'^[A-Z]{3}$')


@app.get('/api/rate')
def rate():
    """GET /api/rate?from=USD&to=EUR: the current exchange rate between two currencies."""
    source = request.args.get('from', '').strip().upper()
    target = request.args.get('to', '').strip().upper()
    if not CURRENCY.match(source) or not CURRENCY.match(target):
        return fail('Use 3-letter currency codes, like USD or EUR.')
    return jsonify(call_api('exchangerate', {'currency1': source, 'currency2': target}))


# The page. On Vercel the CDN serves public/ before a request reaches this app;
# these routes serve it when you run the app locally.
@app.get('/')
def index():
    return send_from_directory(PUBLIC, 'index.html')


@app.get('/<path:name>')
def static_file(name):
    return send_from_directory(PUBLIC, name)


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 3000)), debug=True)
