from datetime import date
import sys
import inflect


def main():
    print(seasons(input("Date of Birth: ")))


def seasons(dt):
    p = inflect.engine()
    try:
        delta = date.today() - date.fromisoformat(dt)
        return f"{p.number_to_words(minutes(delta.days), andword="")} minutes".capitalize()
    except ValueError:
        sys.exit("Invalid date")


def minutes(days):
    return days * 60 * 24


if __name__ == "__main__":
    main()
