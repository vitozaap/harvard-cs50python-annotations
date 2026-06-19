import sys


def main():
    try:
        # Exiting the code prematurely
        if len(sys.argv) > 2:
            sys.exit("Too many arguments")
        print(f"Hello, {sys.argv[1].capitalize()}")

    except IndexError:
        print("No arguments provided. Try again.")


main()
