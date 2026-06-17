def main():
    size = int(input("size: "))

    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # printing brick (no new line)
            print("#", end="")
        print()

    print()
    # same thing but way cleaner
    for _ in range(size):
        print("#" * size)


main()
