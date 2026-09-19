#!/usr/bin/env python3
"""
Currency conversion from the command line.

    python converter.py 100 USD EUR    # one conversion
    python converter.py                # keep converting until you type quit

Reads APIVERVE_API_KEY from .env, like the web app.
"""
import sys

from apiverve import ApiError, call_api


def convert(amount, source, target):
    d = call_api('exchangerate', {'currency1': source.upper(), 'currency2': target.upper()})
    rate = float(d['exchangeRate'])
    print(f"\n  {amount:,.2f} {d['currency1']} = {amount * rate:,.2f} {d['currency2']}")
    print(f"  1 {d['currency1']} = {rate} {d['currency2']}\n")


def interactive():
    print("Currency converter. Type 'quit' to exit.\n")
    while True:
        line = input('Amount and currencies (e.g. 100 USD EUR): ').strip()
        if line.lower() in ('quit', 'exit', 'q'):
            return
        parts = line.split()
        if len(parts) != 3:
            print('  Enter an amount, then two currency codes.\n')
            continue
        try:
            convert(float(parts[0]), parts[1], parts[2])
        except ValueError:
            print('  The amount must be a number.\n')
        except ApiError as err:
            print(f'  Error: {err}\n')


def main():
    if len(sys.argv) == 4:
        try:
            convert(float(sys.argv[1]), sys.argv[2], sys.argv[3])
        except ValueError:
            raise SystemExit('Usage: python converter.py <amount> <from> <to>')
        except ApiError as err:
            raise SystemExit(f'Error: {err}')
    else:
        interactive()


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
