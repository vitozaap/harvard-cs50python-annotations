import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = [generate_integer(level) for _ in range(2)]
        result = x + y
        errors = 0

        while errors != 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer < 0 or answer != result:
                    raise ValueError
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                if errors >= 2:
                    print(f"{x} + {y} = {result}")
                errors += 1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (not level in [1, 2, 3]):
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
