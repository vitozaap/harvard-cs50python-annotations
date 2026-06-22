import sys


def main():
    print(lines_of_code())


def lines_of_code():
    count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    file = sys.argv[1]
    try:
        with open(file) as f:
            for lines in f:
                if not lines.isspace() and not lines.strip().startswith("#"):
                    count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")
    return count


if __name__ == "__main__":
    main()
