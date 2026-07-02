import random

names = ["Harry", "Hermione", "Ron", "Victor"]

students = [
    {"name": name, "house": random.choice(["Gryffindor", "Slytherin"])}
    for name in names
]

for student in students:
    print(student["name"], student["house"])


# You can also do comprehensions to dicts
# Yeah, I can pass a variable as a key
dict_students = {s["name"]: s["house"] for s in students}

print(dict_students)
