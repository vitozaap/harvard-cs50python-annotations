def main():
    tweet = input("Tweet: ")
    print(shorten(tweet))


def shorten(tweet):
    short = ""
    for c in tweet:
        if (c not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]):
            short += c
    return short


if __name__ == "__main__":
    main()
