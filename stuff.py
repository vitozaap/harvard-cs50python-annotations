balance = 0


# Global variables can only be read, cannot be assigned
def main():
    # Can be done!
    print(balance)


def deposit(n):
    # Refers the global variable "balance"
    global balance
    # Cant be done without the "global" keyword.
    balance += n


# Its a convention to declare so called "constants" in uppercase
MEOWS = 3
for _ in range(MEOWS):
    print("meow")

if __name__ == "__main__":
    main()
