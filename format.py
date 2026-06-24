import re


def main():
    get_username()
    name = input("Your name: ").strip()
    # Walrus operator (:=) means: Assign if and only if the value is Truthy
    if matches := re.search(r"^(\w+), *(\w+)$", name, flags=re.IGNORECASE):
        last, first = matches.groups()
        print(f"Hello, {first} {last}")
    else:
        print(f"Hello, {name.title()}")


def get_username():
    url = input("Twitter url: ")
    username = re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE)
    print(username.group(1))


if __name__ == "__main__":
    main()
