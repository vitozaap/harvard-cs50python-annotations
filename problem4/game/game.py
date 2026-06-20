from random import randint


def main():
    game()


def game():
    right = True
    while right:
        try:
            lvl = int(input("Level: "))
        except ValueError:
            pass
        if lvl > 0:
            rand = randint(1, lvl)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess <= 0:
                        raise ValueError()
                    if guess > rand:
                        print("Too large!")
                    elif guess < rand:
                        print("Too small!")
                    else:
                        print("Just Right!")
                        right = False
                        break
                except ValueError:
                    pass


main()
