def main():
    message = input("Greetings: ")
    print(promiseToNotGreeted(message))


def promiseToNotGreeted(message):
    formattedMessage = message.lower().strip()
    if formattedMessage.find("hello") == 0:
        return "$0"
    elif formattedMessage.find("h") == 0:
        return "$20"
    else:
        return "$100"



main()
