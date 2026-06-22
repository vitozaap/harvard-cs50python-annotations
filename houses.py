import csv
from sys import argv

filename = "houses.csv"


def main():
    write(filename)
    students = []
    with open(filename) as f:
        for line in f:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})

    # Using lambda functions (similar to arrow functions) that receive a argument then return its key="name"'s value.
    # So, for each element on students (so called student), the lambda will then return the value of the field "name".
    # I could've created a function that returns the studend["name"] aswell, but a lambda is fine.
    for s in sorted(students, key=lambda student: student["name"]):
        print(f"{s['name']} house's is {s['house']}")


# Same thing but using the csv package to read from file.
# Note: The csv package handles escaped text like when you want to use comma as a TEXT not as a divisor. Just use the quotes "Some, text".
def with_csv():
    write_csv(filename)
    students = []
    with open(filename) as f:
        # You can define the Dict structure at the very first line of the .csv file, so the DictReader can parse it to you to use.
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)

    for s in sorted(students, key=lambda s: s["name"]):
        print(s["name"])


def write(file):
    name = input("Name: ")
    house = input("House ")
    with open(file, "a") as f:
        f.write(f"{name},{house}\n")


def write_csv(file):
    # The csv packages can also writes data to me
    # I need to use newline="" because writer uses \r\n and so windows do with open()
    name = input("Name: ")
    house = input("House: ")
    with open(file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "house"])
        writer.writerow({"name": name, "house": house})


if __name__ == "__main__":
    if argv[1] == "--use-csv":
        print("Using CSV Reader...")
        with_csv()
    else:
        main()
