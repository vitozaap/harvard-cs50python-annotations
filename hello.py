# Creating function
def say_my_name(name):
    # Splits the string using a whitespace as the key character, then assigns those substrings to variables (first, last) in order
    first, last = name.split(" ")
    # Using string datatype methods strip() remove the whitespace (start and end) and capitalize() capitalize the first character
    print(f"Hello, {name.strip().capitalize()}")
    # Prints the user using the title() string method
    print(f"Hello, (now in title mode) {name.title()}")
    # Prints the first and then the last name of the user
    print(f"firstname: {first}\nlastname: {last}")
    return f"firstname: {first} \nlastname: {last}"


if __name__ == "__main__":
    # Calling the function that ive created
    say_my_name(input("Whats your full name: ").strip())
