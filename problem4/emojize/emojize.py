import emoji


def main():
    print(emojize())


def emojize():
    message = input("Input: ")
    return f"Output: {emoji.emojize(message, language='alias')}"


main()
