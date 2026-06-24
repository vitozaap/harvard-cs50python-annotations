from validator_collection import validators, errors


def main():
    print(response(input("Email: ")))


def response(email):
    try:
        validators.email(email)
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()
