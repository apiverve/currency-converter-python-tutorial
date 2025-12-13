#!/usr/bin/env python3
"""
Currency Converter - Tutorial Example

A simple CLI tool that converts between currencies using the APIVerve API.
https://apiverve.com/marketplace/exchangerate
"""

import requests
import sys

# ============================================
# CONFIGURATION - Add your API key here
# Get a free key at: https://dashboard.apiverve.com
# ============================================
API_KEY = 'your-api-key-here'
API_URL = 'https://api.apiverve.com/v1/exchangerate'


def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """
    Convert an amount from one currency to another.

    Args:
        amount: The amount to convert
        from_currency: Source currency code (e.g., 'USD')
        to_currency: Target currency code (e.g., 'EUR')

    Returns:
        Dictionary with conversion results
    """
    if API_KEY == 'your-api-key-here':
        return {'error': 'API key not configured. Add your key to converter.py'}

    try:
        response = requests.get(
            API_URL,
            params={
                'currency1': from_currency.upper(),
                'currency2': to_currency.upper()
            },
            headers={
                'x-api-key': API_KEY
            }
        )

        data = response.json()

        if data.get('status') == 'ok':
            rate = float(data['data']['exchangeRate'])
            converted = amount * rate

            return {
                'success': True,
                'amount': amount,
                'from': from_currency.upper(),
                'to': to_currency.upper(),
                'rate': rate,
                'result': round(converted, 2)
            }
        else:
            return {'error': data.get('error', 'Conversion failed')}

    except requests.RequestException as e:
        return {'error': f'API request failed: {str(e)}'}
    except (KeyError, ValueError) as e:
        return {'error': f'Invalid response: {str(e)}'}


def print_result(result: dict):
    """Print conversion result in a formatted way."""
    if 'error' in result:
        print(f"\n❌ Error: {result['error']}\n")
    else:
        print(f"\n{'='*40}")
        print(f"  {result['amount']:,.2f} {result['from']}")
        print(f"  = {result['result']:,.2f} {result['to']}")
        print(f"{'='*40}")
        print(f"  Exchange Rate: 1 {result['from']} = {result['rate']} {result['to']}")
        print()


def interactive_mode():
    """Run the converter in interactive mode."""
    print("\n" + "="*40)
    print("  Currency Converter")
    print("  Powered by APIVerve")
    print("="*40)
    print("\nType 'quit' to exit\n")

    while True:
        try:
            # Get amount
            amount_input = input("Amount to convert: ").strip()
            if amount_input.lower() == 'quit':
                break

            try:
                amount = float(amount_input)
            except ValueError:
                print("Invalid amount. Please enter a number.\n")
                continue

            # Get currencies
            from_currency = input("From currency (e.g., USD): ").strip()
            if from_currency.lower() == 'quit':
                break

            to_currency = input("To currency (e.g., EUR): ").strip()
            if to_currency.lower() == 'quit':
                break

            # Convert
            result = convert_currency(amount, from_currency, to_currency)
            print_result(result)

        except KeyboardInterrupt:
            print("\n")
            break

    print("Goodbye!\n")


def main():
    """Main entry point."""
    if len(sys.argv) == 4:
        # Command line mode: python converter.py 100 USD EUR
        try:
            amount = float(sys.argv[1])
            from_currency = sys.argv[2]
            to_currency = sys.argv[3]

            result = convert_currency(amount, from_currency, to_currency)
            print_result(result)
        except ValueError:
            print("Usage: python converter.py <amount> <from_currency> <to_currency>")
            print("Example: python converter.py 100 USD EUR")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == '__main__':
    main()
