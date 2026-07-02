# Generators in python can delivery data piece by piece
# They are very similar to Observables in rxjs


def main():
    # Will call __next__ everytime time until it does not have any values remaining
    for s in sheep(10):
        print(s)


def sheep(n):
    for i in range(n):
        # Yield you return one thing at the time
        yield "🐑" * i


main()
