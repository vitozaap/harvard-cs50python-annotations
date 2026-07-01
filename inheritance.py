def main():
    me = Wizard("Victor", 19)
    professor = Professor("Victor", 58, "Data Science")
    student = Student("Victor", 18, "Gryffindor")
    print(me, student, professor)


class Wizard:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Wizard): # Class(Superclass)
    def __init__(self, name, age, house):
        # super will refers to the superclass "Wizard"
        super().__init__(name, age)
        self.house = house


class Professor(Wizard): # Class(Superclass)
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


if __name__ == "__main__":
    main()
