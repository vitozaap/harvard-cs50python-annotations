def main():
    tweet = input("Tweet: ")
    setting_my_twttr(tweet)

def setting_my_twttr(tweet):
    for c in tweet:
        if (c.lower() not in ["a", "e", "i", "o", "u"]):
            print(c, end="")
    print()


main()
