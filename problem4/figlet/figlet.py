from sys import exit, argv
from random import choices
from pyfiglet import Figlet


def main():
    figlet()


def figlet():
    figlet = Figlet()
    fonts = figlet.getFonts()
    arguments = ["-f", "--font"]
    if len(argv) == 3:
        if argv[1] in arguments and argv[2] in fonts:
            figlet.setFont(font=argv[2])
        else:
            exit("Invalid usage")
    elif len(argv) == 1:
        figlet.setFont(font=choices(fonts)[0])
    else:
        exit("Invalid usage")

    text = input("Text: ")
    print(figlet.renderText(text))


main()
