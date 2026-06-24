import re


def main():
    # Validates gmail.com emails
    # p_email = r"^[^@]+@gmail\.com$"
    """
    . any character except a newline
    * 0 or more repetitions
    + 1 or more repetitions
    ? 0 or 1 repetition
    {m} m repetitinos
    {m,n} m - n repetitions
    ^ matches the start of the string
    $ matches the end of the string or just before the newline at the end of the string
    [] set of characters
    [^] complementing the set (so [^@] would say: everything BESIDES @)
    [a-zA-Z] interval 'a' to 'z' and 'A' to 'Z'
    \w - Word character - represents an alphanumeric symbol and the underscore aswell
    \W - Not a word character
    \d - decimal digit
    \D - not a decimal digit
    \s - whitespace characters
    \S - not a whitespace character
    () a group
    (?:...) non-capturing version
    A|B Represents a tuple, one or other (in this case? 'A' or 'B')
    """
    email = input("Email: ").strip().lower()
    # r"" stands for RAW strings. Python will not try to  any back slashes as scape characters
    # You can pass flags to the re.search() function. 
    if re.search(r"^\w+@\w+\.(?:edu|com|gov)$", email, flags=re.IGNORECASE):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()


p_email = r"^[^@]+@[^@]+\gmail.com$"
