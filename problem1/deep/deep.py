def main():
    message = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(aswering(message))


def aswering(message):
    match message.lower().replace("-", " ").strip():
        case "forty two" | "42":
            return "Yes"
        case _:
            return "No"


main()
