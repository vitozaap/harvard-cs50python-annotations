from cowsay import cow
import sys


def main():
    if len(sys.argv) < 2:
        # Early exit
        sys.exit("Too few arguments")
    cow(f"Hello, {sys.argv[1].capitalize()}")


main()
