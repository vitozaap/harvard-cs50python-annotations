def main():
    fruit = input("Item: ").title()
    nutrition(fruit)


def nutrition(item):
    fruits = {
        "Apple": "130", "Banana": "110", "Avocado": "50",
        "Cantaloupe": "50", "Grapefruit": "60", "Grapes": "90",
        "Honeydew Melon": "50", "Kiwifruit": "90", "Lemon": "15",
        "Nectarine": "60", "Orange": "80", "Peach": "60",
        "Pear": "100", "Pineapple": "50", "Plums": "70",
        "Strawberries": "50", "Sweet Cherries": "100", "Tangerine": "50",
        "Watermelon": "80", "Lime": "20"
    }

    if item in fruits:
        print(f"Calories: {fruits[item]}")


main()
