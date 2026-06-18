def main():
    grocery()


def grocery():
    grocery_list: dict = {}
    while True:
        try:
            item = input().lower().strip()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            print()
            for i in sorted(grocery_list):
                print(f"{grocery_list[i]} {i.upper()}")
            break
        except KeyError:
            pass


main()
