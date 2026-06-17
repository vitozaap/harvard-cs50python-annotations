def main():
    message = input("camelCase: ")
    to_snake_case(message)


def to_snake_case(message):
    for character in message:
        if character.isupper():
            print(f"_{character.lower()}", end="")
        else:
            print(character, end="")
    print()

main()
