def main():
    print(fuel_porcentage())


def fuel_porcentage():
    while True:
        fuel = input("Fuel: ")
        try:
            x, y = fuel.split("/")
            dividend, divisor = int(x), int(y)
            calc = dividend / divisor
            if calc > 1 or dividend < 0 or divisor < 0:
                raise ValueError()
            elif calc < 0.1:
                return "E"
            elif calc >= 0.99:
                return "F"
            else:
                return f"{round(calc * 100)}%"

        except (ValueError, ZeroDivisionError):
            print("Something went wrong.")


main()
