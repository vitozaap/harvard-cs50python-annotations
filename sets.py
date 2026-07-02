def main():
    students = [
        {
            "name": "Victor",
            "house": "Gryffindor",
        },
        {
            "name": "Harry",
            "house": "Gryffindor",
        },
        {
            "name": "Hermione",
            "house": "Gryffindor",
        },
        {
            "name": "Draco",
            "house": "Slytherin",
        },
    ]
    # A set will automatically remove duplicates from it
    houses = set()
    for student in students:
        if student["house"] not in houses:
            houses.add(student["house"])

    for house in sorted(houses):
        print(house)


if __name__ == "__main__":
    main()
