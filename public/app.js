import { api, busy, esc, showError, stats } from './ui.js';

// Any 3-letter code the API supports works; these are the ones in the menus.
const CURRENCIES = {
  USD: 'US dollar', EUR: 'Euro', GBP: 'British pound', JPY: 'Japanese yen', CAD: 'Canadian dollar',
  AUD: 'Australian dollar', CHF: 'Swiss franc', CNY: 'Chinese yuan', INR: 'Indian rupee', MXN: 'Mexican peso',
  BRL: 'Brazilian real', ZAR: 'South African rand', SEK: 'Swedish krona', NOK: 'Norwegian krone',
  NZD: 'New Zealand dollar', SGD: 'Singapore dollar', HKD: 'Hong Kong dollar', KRW: 'South Korean won',
  PLN: 'Polish złoty', TRY: 'Turkish lira', AED: 'UAE dirham'
};

const form = document.getElementById('form');
const amount = document.getElementById('amount');
const from = document.getElementById('from');
const to = document.getElementById('to');
const go = document.getElementById('go');
const result = document.getElementById('result');

const options = Object.entries(CURRENCIES)
  .map(([code, name]) => `<option value="${code}">${code} · ${esc(name)}</option>`)
  .join('');
from.innerHTML = options;
to.innerHTML = options;
from.value = 'USD';
to.value = 'EUR';

const money = (value, code) =>
  new Intl.NumberFormat(undefined, { style: 'currency', currency: code }).format(value);

document.getElementById('swap').addEventListener('click', () => {
  [from.value, to.value] = [to.value, from.value];
  if (result.innerHTML) form.requestSubmit();
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const value = Number(amount.value);
  if (!(value >= 0)) return showError(result, 'Enter an amount to convert.');
  const query = new URLSearchParams({ from: from.value, to: to.value });
  busy(go, 'Converting…', async () => {
    try {
      const d = await api(`/api/rate?${query}`);
      const rate = Number(d.exchangeRate);
      result.innerHTML = `
        <div class="figure">
          <div class="sub">${esc(money(value, d.currency1))} =</div>
          <div class="big">${esc(money(value * rate, d.currency2))}</div>
        </div>
        ${stats([
          ['Rate', `1 ${d.currency1} = ${rate} ${d.currency2}`],
          ['Inverse', `1 ${d.currency2} = ${(1 / rate).toPrecision(6)} ${d.currency1}`],
          ['Updated', d.lastUpdated && new Date(d.lastUpdated).toLocaleString()]
        ])}`;
    } catch (err) {
      showError(result, err);
    }
  });
});
