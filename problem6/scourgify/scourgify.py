import csv
import sys


def main():
    scourgify()


def scourgify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    file = sys.argv[1]
    new_file = sys.argv[2]
    try:
        with open(file) as f:
            reader = csv.DictReader(f)
            with open(new_file, "w", newline="") as new_f:
                writer = csv.DictWriter(
                    new_f, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for line in reader:
                    last, first = line["name"].split(",")
                    writer.writerow(
                        {"first": first.strip(), "last": last.strip(), "house": line["house"]})

    except FileNotFoundError as error:
        sys.exit(f"Could not read {error.filename}")


if __name__ == "__main__":
    main()
