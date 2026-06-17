def main():
    i = 0

    # Its fine to use infinity loop here because I have a statement to break or continue it
    while True:
        num = int(input("Meow times: "))
        if num > 0:
            break
        print("Number cant be less or equal 0")

    while i < 3:
        print("meow with while")
        i += 1  # Python doesnt have ++ or --, just += and -= (kinda sad.)

    for value in [0, 1, 2]:
        print("meow in list range")

    # range() produces a list sized by the limit you passed to it.
    # [0, 1, 2, 3] and so forth
    for i in range(3):
        print("meow in range()")

    for _ in range(1):
        print("not using the variable so I use underscore _")
    # so it concatenates meow by 3 times. set end="" so will not have a \n at the end
    print("meow in print \n" * num, end="")

    # Just playing with lists and for loops
    students = ["Victor", "Kalel", "Marcelo"]
    for student in students:
        print(student)

    for i in range(len(students)):
        print(f"{i} is {students[i]}")


main()
