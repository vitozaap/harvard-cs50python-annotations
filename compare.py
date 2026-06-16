def main():
    n = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    print(comparingTwoNumbers(n, n2))
    if is_even(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


def comparingTwoNumbers(n=0, n2=0):
    """
    In python we use "and" and "or" or "&"" and "|"
    So and = &
       or = |
    """
    if n == n2:
        return f"{n} is equal to {n2}"
    elif n2 > n & n < 100:
        return f"{n2} is greater than n and n is less than 100"
    elif n > n2:
        return f"{n} is greater than {n2}"
    elif n2 > n:
        return f"{n2} is greater than {n}"
    else:
        return "Something went wrong"


# Returning boolean values (weird that it uses Capitals lol) All examples are the same thing
def is_even(n):
    # return True if n% 2 == 0 else False
    """
    if n% 2 == 0:
        return True
    else:
        return False
    """
    return n % 2 == 0 

main()
