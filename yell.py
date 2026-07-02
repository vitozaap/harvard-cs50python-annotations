def yell(*s):
    # Map will apply the function to each of the arguments
    uppercase = map(lambda item: item.upper(), s)
    print(*uppercase)


yell("this is cs50")


def list_comprehensions(*strings, **kwargs):
    # Do basically the same as the map function, but on the fly
    lower = [word.upper() for word in strings]

    # access the value from the list of dicts
    print([k.lower() for k in kwargs])
    return lower


print(list_comprehensions("asds", named=1))


students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Now I will create a new list that containsn only the students from "students" list that match the if statement
gryffindors = [ student["name"] for student in students if student["house"] == "Gryffindor" ]

# The lambda function will eventually run for each student of students list. Students will be iterate and passed as argument to the function
for s in filter(lambda student: student["house"] == "Gryffindor", students):
    print(s["name"])
    


