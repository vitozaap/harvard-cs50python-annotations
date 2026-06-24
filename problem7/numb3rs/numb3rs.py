import re


def main():
    ip = input("Ip address: ")
    print(validate(ip))


def validate(ip):
    pattern = r"^(([0-9][0-9]?|1[0-9]{1,2}|2([0-4][0-9]|[0-5]{2})?)\.){3}([0-9][0-9]?|1[0-9]{1,2}|2([0-4][0-9]|[0-5]{2})?)$"
    if re.search(pattern, ip):
        return True
    return False


if __name__ == "__main__":
    main()
