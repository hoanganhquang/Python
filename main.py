from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()

money = MoneyMachine()

_continue = True
while _continue:
    choice = menu.get_items()
    type_coffee = input(f"What would you like? {choice}: ").lower()
    if type_coffee == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(type_coffee)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    _continue = True



