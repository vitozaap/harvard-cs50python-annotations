def main():
    vault1 = Vault(10, 15, 20)
    vault2 = Vault(30, 40, 50)
    print(vault1 + vault2)


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # ----- Operator Overloading -----
    # This method will automatically be called wether the "+" operator is used
    # Python will try both sides __add__ method, and will choose between the implementations
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        knuts = self.knuts + other.knuts
        sickles = self.sickles + other.sickles
        return Vault(galleons, sickles, knuts)

    def __sub__(self, other):
        galleons = self.galleons - other.galleons
        knuts = self.knuts - other.knuts
        sickles = self.sickles - other.sickles
        return Vault(galleons, sickles, knuts)

    def __str__(self):
        return f"Vault ballance \nGalleons: {self.galleons} Sickles: {self.sickles} Knuts: {self.knuts}"


if __name__ == "__main__":
    main()
