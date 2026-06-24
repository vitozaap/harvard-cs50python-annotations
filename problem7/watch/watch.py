import re


def main():
    s = input("Url: ")
    print(parse(s))


def parse(s):
    pattern = r'^<iframe.*src="https?://(?:www\.)?youtube\.com/embed/(\w+)"'
    if matches := re.search(pattern, s):
        return f"https://youtu.be/{matches.group(1)}"
    return None

if __name__ == "__main__":
    main()
