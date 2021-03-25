from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
options = menu.get_items()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
is_on = True
while is_on:
    user_input = input(f"What would you like? ({options}): ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        choice = menu.find_drink(user_input)
        if choice != None:
            if money_machine.make_payment(choice.cost) and coffe_maker.is_resource_sufficient(choice):
                coffe_maker.make_coffee(choice)
