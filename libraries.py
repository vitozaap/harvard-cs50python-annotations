# Couldve done `import random`
from random import choice, randint, shuffle


def main():
    randomizing_things()


def randomizing_things():
    names = ["Victor", "Marcelo", "Kalel", "Phelipe", "Gabriel"]
    print(choice(range(100)))
    print(randint(1, 100))
    # Shuffle literally shuffles a list then returns None
    shuffle(names)
    for name in names:
        print(name)
    print(names)


main()
