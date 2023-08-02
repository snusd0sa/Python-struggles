MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check_resources(drink):
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
if choice == "report":
    print_report()
elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
    drink = MENU[choice]
    if check_resources(drink):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.1 + nickel * 0.05 + pennies * 0.01
        if total < drink["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money += drink["cost"]
            for ingredient in drink["ingredients"]:
                resources[ingredient] -= drink["ingredients"][ingredient]
            print(f"Here is ${round(total - drink['cost'], 2)} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
