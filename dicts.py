def main():
    # key value pair is called dict in python
    students = {"Hermione": "Gryffindor", "Harry": "Gryffindor"}

    # Prints its values using [] then the key name
    print(students["Harry"])

    # Prints all values one by one
    for key in students:
        print(f"key: {key}; value: {students[key]}")

    # Prints all keys one by one
    for key in students:
        print(f"key: {key}")


main()
