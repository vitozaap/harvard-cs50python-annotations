import statistics
import sys


def main():
    average()


def average():
    # argv (arguments vector) extract all arguments passed when running the .py file. argv[0] is the name of the file.
    print(sys.argv)
    print(statistics.mean([10, 9.5, 9, 10]))


main()
