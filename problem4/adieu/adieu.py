import inflect


def main():
    adieu()


def adieu():
    names = []
    p = inflect.engine()
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break
    print(f"Adieu, adieu, to {p.join(names)}")


main()
