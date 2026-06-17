def main():
    # creating a list of object called student
    students = [
        {"name": "Harry", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Stag"},
    ]

    ron = {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"}
    print(f"object Ron's patronus: {ron['patronus']}")
    # I can access the corresponding value of any key using the same syntax as trying to access values of key value pairs
    for student in students:
        print(f"for loop in students: {student['patronus']}")

    # Can also access either the positions and the value of any key using two square brackets together (first position, second key)
    for i in range(len(students)):
        print(f"i of range loop: {students[i]['name']}")


main()
