import csv
import sys
from tabulate import tabulate


def main():
    pizza()


def pizza():
    table = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    file = sys.argv[1]
    try:
        with open(file) as f:
            r = csv.DictReader(f)
            for lines in r:
                t_table = []
                for header in r.fieldnames:
                    t_table.append(lines[header])
                table.append(t_table)
            print(tabulate(table, headers=r.fieldnames, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
