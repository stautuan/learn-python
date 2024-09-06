"""
Implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins, n, that they 
would like to buy. If that argument cannot be converted to a float, the program should exit 
via sys.exit with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, 
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
Be sure to catch any exceptions. 
"""

import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)

    for arg in sys.argv[1:]:
        if not is_floatstring(arg):
            sys.exit("Command-line argument is not a number")

        bitcoin_price = get_bitcoin_price()
        amount = bitcoin_price * float(arg)
        print(f"${amount:,.4f}")


def is_floatstring(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def get_bitcoin_price():
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = response.json()
    return bitcoin["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()
