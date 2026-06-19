from cowsay import cow

# importing the module ive just created
import greetings


def main():
    cow(greetings.hello("Victor"))
    cow(greetings.goodbye("Zap"))


main()
