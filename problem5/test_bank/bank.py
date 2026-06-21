def main():
    message = input("Greetings: ")
    print(f"${promiseToNotGreeted(message)}")


def value(message):
    formattedMessage = message.lower().strip()
    if formattedMessage.find("hello") == 0:
        return 0
    elif formattedMessage.find("h") == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
