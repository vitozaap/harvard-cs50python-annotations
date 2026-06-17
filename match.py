def main():
    print(matching_names(input("Your name: ")))


# Using match cases (switch cases) and using "or" statement | 
def matching_names(name):
    match name.capitalize():
        case "Victor" | "Zap":
            return "Its me!"
        case "Mom" | "Mommy":
            return "Hi, mom!"
        case "Dad" | "Daddy":
            return "Hi, dad!"
        # A non handled case uses "_"
        case _:
            return f"Do I know you, {name}?"


main()
