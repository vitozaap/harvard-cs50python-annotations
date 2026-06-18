def main():
    value = get_int("Value: ")
    print(value)
    while True:
        # Same as "try catch" blocks but not "try except"
        try:
            x = int(input("Number: "))
        except ValueError:
            print("x in not a valid value.")
        # Only occurs if there is no exceptions
        else:
            print(f"x is: {x}")
            break


def get_int(message="Message"):
    while True:
        try:
            return int(input(message))
        except ValueError:
            # You can just pass this error, if you dont want to handle it
            pass


main()
