import requests
from sys import argv, exit


def main():
    print(calculate_bitcoin())


def calculate_bitcoin():
    try:
        price = float(requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=249873c3b5ccc6ba43b32e0166425fefc3ed55b463a4efc499e456f10f33ff86").json()["data"]["priceUsd"])
        try:
            amount = float(argv[1])
        except ValueError:
            exit("Command-line argument is not a number")

        return f"${price * amount:,.4f}"
    except requests.RequestException:
        exit()
    except IndexError:
        exit("Missing command-line argument")


main()
