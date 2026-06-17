def main():
    message = input("What time is it? ")
    decimalTime = convert(message)
    if (7 <= decimalTime <= 8):
        print("breakfast time")
    elif (12 <= decimalTime <= 13):
        print("lunch time")
    elif (18 <= decimalTime <= 19):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    decimal = int(hours) + int(minutes) / 60
    return decimal


if __name__ == "__main__":
    main()
