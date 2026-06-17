def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    is_correct_Length = 2 <= len(s) <= 6

    if s.isalpha() and is_correct_Length:
        return True

    if s.isalnum() and s[0:2].isalpha() and is_correct_Length:
        for c in range(len(s)):
            if s[c].isnumeric():
                indexFirstNumber = c
                break
        if s[indexFirstNumber:].isnumeric() and s[indexFirstNumber] != "0":
            return True
    return False


main()
