def main():
    message = input("Message: ")
    print(convert(message))


def convert(message):
    return message.replace(":)", "🙂").replace(":(", "🙁")


main()
