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
    }
}

PROFIT = 0
REMAINING_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    """prints current remaining resources"""
    print(f"Water: {REMAINING_RESOURCES['water']}")
    print(f"Milk: {REMAINING_RESOURCES['milk']}")
    print(f"Coffee: {REMAINING_RESOURCES['coffee']}")
    print(f"Money: ${PROFIT}")


def take_money():
    """ returns total money given"""
    quarters = int(input("How many quarters? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (nickels * 0.1) + \
        (dimes * 0.05) + (pennies * 0.01)
    return round(total, 2)


def take_resources(drink, money):
    """takes type of drink as input and returns true if there are enough resources, false if not"""
    for ingredient, total in MENU[drink]["ingredients"].items():
        if REMAINING_RESOURCES[ingredient] < total:
            print(
                f"Sorry There's not enough {ingredient}, ${money} has been refunded.")
            return False
        else:
            REMAINING_RESOURCES[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here's your {drink}, enjoy!")
    return True


def add_resources():
    """adds to remaining resources"""
    for resource in REMAINING_RESOURCES:
        REMAINING_RESOURCES[resource] += int(
            input(f"How much {resource} do you want to add? "))


while True:
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print_report()
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        money = take_money()
        if money < MENU[user_choice]["cost"]:
            print(f"Sorry that's not enough money. ${money} refunded.")
        else:
            change = money - MENU[user_choice]["cost"]
            enough_resources = take_resources(user_choice, money)
            if enough_resources:
                if change > 0:
                    print(f"Here's ${round(change, 2)} in change")
                PROFIT += MENU[user_choice]["cost"]
    elif user_choice == "topup":
        add_resources()
        print("The coffee machine has been topped up!")
    elif user_choice == "off":
        break
    else:
        print(f"{user_choice} is not valid!")
