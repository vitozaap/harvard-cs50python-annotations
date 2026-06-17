# defining the main function is a better practice to describe the main code of my program
def main():
    # Using try and expect to handle errors
    try:
        # Using the int() function to convert string into int so the values can be calculated properly
        num = int(input("Type the first number: "))
        num2 = int(input("Type the second number: "))

    except ValueError:
        raise ValueError("You must provide a integer to continue.")
    # else used be the try expect block
    else:
        print(num + num2)

    # Will use default parameters values (1.0, 1.0)
    calculate_with_float_values()

    # Will use the values that ive passed to it
    calculate_with_float_values(2.0, 3.0)

    # Printing the subtraction returning value
    print(subtraction(128, 64))


# Defining function with default parameters values
def calculate_with_float_values(float1=1.0, float2=1.0):

    # Uses the built-in function round() to round the calculation result by two digits
    print(f"rounded by 2 digits: {round((float1 + float2), 2)}")

    # Using if else block to validate if the calculation is less than 999
    if float1 + float2 < 999:
        print(
            "The result of the provided floats is not greater than 1000 to be separeted with comma. Try again with much greater numbers."
        )
    else:
        # Formatting numbers using f strings defining that I want to add comma to large numbers
        print(f"separating large numbers with comma: {round(float1 + float2):,}")


def subtraction(num, num2):
    return int(num) - int(num2)


# Calling the main function
main()
