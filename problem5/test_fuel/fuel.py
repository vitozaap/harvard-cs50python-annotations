def main():
    porcentage = convert(input("Fuel: "))
    gauge(porcentage)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    calc = round(x / y * 100)
    if x > y or x < 0 or y < 0:
        raise ValueError
    return calc


def gauge(porcentage):
    if porcentage <= 1:
        return "E"
    elif porcentage >= 99:
        return "F"
    else:
        return f"{porcentage}%"


if __name__ == "__main__":
    main()
