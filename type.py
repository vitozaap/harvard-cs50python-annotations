import random


def main():
    me = Student("Victor")
    # AS the class is a singleton, I can just call it an use a @classmethod method without create a new object of this class in question.
    Hat.sort(me)
    print(me)


class Student:
    def __init__(self, name, house=""):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self._name} is from {self._house}."

    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw", ""]:
            raise ValueError("Invalid house")
        self._house = house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name


# Will be defined as a singleton, a class that has no need to be instantiated or have multiple objects of
class Hat:
    # A class variable, exist in a global scope of the class
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod  # Defines a class method that can be used without being instantiated. This method belongs to the class, not to the object
    # class methods can be used as custom constructors.
    def sort(cls, student):  # cls refers to the class itself
        student.house = random.choice(cls.houses)
        return f"{student.name} now has his own house defined. Check it now!"


class Test:
    def __init__(self, name):
        self.name = name

    @classmethod
    def get(cls):
        name = input("Name: ")
        # It will instantiate a new instance of the class itself and returns it
        return cls(
            name
        )  


if __name__ == "__main__":
    main()
