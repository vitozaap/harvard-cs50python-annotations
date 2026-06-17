def main():
    table(get_positive_number("Table of? "))


def get_positive_number(message="Positive number: "):
    # Python does not create a new scope in loops.
    # Thats why I can access the value of "n" off the loop but inside the function
    while True:
        n = int(input(message))
        if n > 0:
            break
    return n


def table(n):
    i = 1
    while i <= 10:
        print(f"{n} * {i} = {n * i}")
        i += 1


main()
