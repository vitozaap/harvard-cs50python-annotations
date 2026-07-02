students = ["Harry", "Hermione", "Ron"]

# Enumerate function will enumerate with a tuple (num, value) for a iterable object.
for i in enumerate(students, start=1):
    print(*i)
