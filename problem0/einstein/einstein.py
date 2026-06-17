def main():
    mass = int(input("Mass (kg): "))
    print(calculateJoules(mass))


def calculateJoules(mass):
    return mass * pow(300000000, 2)


main()
