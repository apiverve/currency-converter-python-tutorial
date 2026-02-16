# Currency Converter | APIVerve API Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![APIVerve | Exchange Rate](https://img.shields.io/badge/APIVerve-Exchange_Rate-purple)](https://apiverve.com/marketplace/exchangerate?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial)

A simple Python CLI tool that converts between 150+ currencies in real-time. Perfect for finance apps, e-commerce, or learning API integration with Python.

![Screenshot](https://raw.githubusercontent.com/apiverve/currency-converter-python-tutorial/main/screenshot.jpg)

---

### Get Your Free API Key

This tutorial requires an APIVerve API key. **[Sign up free](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial)** - no credit card required.

---

## Features

- Convert between 150+ world currencies
- Real-time exchange rates
- Interactive CLI mode
- Command-line arguments for scripting
- Clean, readable Python code
- Minimal dependencies (just `requests`)

## Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/apiverve/currency-converter-python-tutorial.git
   cd currency-converter-python-tutorial
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key**

   Open `converter.py` and replace the placeholder with your API key:
   ```python
   API_KEY = 'your-api-key-here'
   ```

4. **Run the converter**

   Interactive mode:
   ```bash
   python converter.py
   ```

   Or with command-line arguments:
   ```bash
   python converter.py 100 USD EUR
   ```

## Usage

### Interactive Mode

```bash
$ python converter.py

========================================
  Currency Converter
  Powered by APIVerve
========================================

Type 'quit' to exit

Amount to convert: 100
From currency (e.g., USD): USD
To currency (e.g., EUR): EUR

========================================
  100.00 USD
  = 92.65 EUR
========================================
  Exchange Rate: 1 USD = 0.9265 EUR
```

### Command-Line Mode

```bash
# Convert 100 USD to EUR
python converter.py 100 USD EUR

# Convert 50 GBP to JPY
python converter.py 50 GBP JPY

# Convert 1000 EUR to USD
python converter.py 1000 EUR USD
```

## Project Structure

```
currency-converter-python-tutorial/
├── converter.py        # Main converter script
├── requirements.txt    # Python dependencies
├── screenshot.jpg      # Preview image
├── LICENSE             # MIT license
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## API Reference

**Endpoint:** `GET https://api.apiverve.com/v1/exchangerate`

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `currency1` | string | Yes | Source currency code (e.g., "USD") |
| `currency2` | string | Yes | Target currency code (e.g., "EUR") |

**Example Response:**

```json
{
  "status": "ok",
  "error": null,
  "data": {
    "currency1": "USD",
    "currency2": "EUR",
    "exchangeRate": "0.926480"
  }
}
```

## Supported Currencies

The API supports 150+ currencies including:

| Code | Currency |
|------|----------|
| USD | US Dollar |
| EUR | Euro |
| GBP | British Pound |
| JPY | Japanese Yen |
| CAD | Canadian Dollar |
| AUD | Australian Dollar |
| CHF | Swiss Franc |
| CNY | Chinese Yuan |
| INR | Indian Rupee |
| MXN | Mexican Peso |

[View full list →](https://apiverve.com/marketplace/exchangerate?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial)

## Customization Ideas

- Add a Flask web interface
- Cache exchange rates with TTL
- Add historical rate lookups
- Create a batch conversion mode
- Export results to CSV
- Add currency symbol formatting

## Related APIs

Explore more APIs at [APIVerve](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial):

- [Currency Converter](https://apiverve.com/marketplace/currencyconverter?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial) - Direct currency conversion
- [Gold Price](https://apiverve.com/marketplace/goldprice?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial) - Current gold prices
- [Silver Price](https://apiverve.com/marketplace/silverprice?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial) - Current silver prices

## License

MIT - see [LICENSE](LICENSE)

## Links

- [Get API Key](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial) - Sign up free
- [APIVerve Marketplace](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial) - Browse 300+ APIs
- [Exchange Rate API](https://apiverve.com/marketplace/exchangerate?utm_source=github&utm_medium=tutorial&utm_campaign=currency-converter-python-tutorial) - API details
