def main():
    student = get_student_class()
    print(student.age, student.name, student.charm())
    print(student)
    get_car()


def get_student():
    # You could return more than 1 value using a tuple (tuples cannot change its values)
    return (input("Name: "), input("House: "))


# You can define classes in python to shape data
class Student:
    # Also possible to define data types (str = string)
    # name: str
    # age: int

    # Basically the constructor of this class
    # "self" is not a param that you can pass, its the current object of the class, you can use it to save data into the object
    def __init__(self, name, age, patronus):
        self.name = name
        self.age = age
        self.patronus = patronus

    # Will run everytime somewhere in the code, you want to see the object as a string
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # By convention, every method from a class have "self" as a parameter, sou you can access the current object.
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case _:  # _ is the "default" case if it does not match any
                return "🪄"


class Car:
    def __init__(self, brand, year):
        self._brand = brand  # Because I defined a setter method, now everytime I reference the class car.brand, it will call the setter function
        self._year = year

    @property  # Defines that THIS function is a getter
    # Getter -> Gets some attribute
    # You should name the function exactly how you want the property to be called
    def brand(self):
        return f"from getter: {self._brand}"

    @brand.setter  # Sets the "brand" function/property value
    # Setter -> Sets some attribute
    # You should also names it as you want the property to be called
    def brand(self, brand):
        if brand not in ["Toyota", "Hyundai", "Fiat"]:
            raise ValueError("Invalid brand")

        # Or the method or the variable can be called like that, so, by convention, variables use the prefix "_" in it: _value
        self._brand = brand

    def __str__(self):
        return f"Your car is a {self._brand} from {self._year}"


def get_car():
    car = Car("Toyota", 2024) # Will call the __init__ method
    car.brand = "Fiat" # Will call setter method "brand.setter"
    print(car.brand) # Will call the getter method "brand"
    print(car._brand) # Will print the current raw attribute value, not passing trhough getter method
    print(car) # Will call the __str__ method
    return car


def get_student_class():
    return Student(
        name=input("Name: "), age=int(input("Age: ")), patronus=input("Patronus: ")
    )


if __name__ == "__main__":
    main()
