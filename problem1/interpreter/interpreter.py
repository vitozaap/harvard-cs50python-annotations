def main():
    message = input("Math expression: ")
    print(interpreter(message))


def interpreter(expression):
    x, y, z = expression.split(" ")
    n = int(x)
    n2 = int(z)
    match y:
        case "+":
            return f"{(n + n2):.1f}"
        case "-":
            return f"{(n - n2):.1f}"
        case "*":
            return f"{n * n2:.1f}"
        case "/":
            return f"{n / n2:.1f}"


main()
