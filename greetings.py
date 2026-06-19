# Everytime I used something from here, main will be executed
def main():
    hello("Testing")
    goodbye("Testing")


def hello(name):
    return f"hello, {name}"


def goodbye(name):
    return f"goodbye, {name}"


# Now main() only will be called if the actual file is being executed from cli.
# __name__ is only set to "__main__" when this file is executed by cli.
if __name__ == "__main__":
    main()
