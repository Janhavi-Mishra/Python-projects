from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()


def coffee_making():
    # TODO: (1) take order
    order_name = input(f"Select a drink: {menu.get_items()}\n").lower()
    order_info = menu.find_drink(order_name)

    # TODO: (2) Check resources sufficient
    enough_resources = coffee_machine.is_resource_sufficient(order_info)
    if enough_resources:

        # TODO: (3) Process coins
        enough_money = money.make_payment(order_info.cost)
        if enough_money:

            # TODO: (4) Make coffee
            coffee_machine.make_coffee(order_info)

    # TODO: (5) Print Report
    coffee_machine.report()

    new_order = input("Do you want to make another order? Yes or No?\n").lower()
    return new_order


flag = "yes"
while flag == "yes":
    flag = coffee_making()
