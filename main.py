import data

MENU = data.MENU
resources = data.resources


# TODO: 3. print report of resources
def resource_report(resources):
    """Return report about resources in machine"""
    print("Resource report: ")
    for resource, value in resources.items():
        if resource == 'coffee':
            print(f"{resource.title()} : {value} g")
        elif resource == 'profit':
            print(f"{resource.title()} : ${value}")
        else:
            print(f"{resource.title()} : {value} ml")


# TODO: 1. print prompt 'what would you like?'
def welcome_text():
    """Takes order from user"""
    print("\nWelcome to the coffee machine!\n")
    i = 1
    for coffee, price in MENU.items():
        print(f"{i}) {coffee.title()} : ${price['cost']}")
        i += 1
    drink = input("What would you like to order? ").lower()
    if drink == 'report':
        return 'report'
    else:
        order = {drink: MENU[drink]}

    return order


# TODO: 4. check if sufficient resources
def check_resources(order, resources):
    """Checks if enough resources are available"""
    store_water = resources['water']
    store_milk = resources['milk']
    store_coffee = resources['coffee']
    drink = list(order.keys())
    water_needed = order[drink[0]]['ingredients']['water']
    milk_needed = order[drink[0]]['ingredients']['milk']
    coffee_needed = order[drink[0]]['ingredients']['coffee']

    if water_needed <= store_water:
        if milk_needed <= store_milk:
            if coffee_needed <= store_coffee:
                return True
            else:
                print("Not enough coffee!")
                return False
        else:
            print("Not enough milk!")
            return False
    else:
        print("Not enough water!")
        return False


# TODO: 5. process coins and check sum
# TODO: 6. check transaction successful
def coin_check(order):
    """Takes money from user and checks if it is enough"""
    print("\nPlease enter the money in the slot!")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_input = quarters + dimes + nickels + pennies
    drink = list(order.keys())
    order_price = order[drink[0]]['cost']
    print(f"You have added ${round(total_input)}. The total price is ${order_price}.")
    if order_price > total_input:
        print("\nYou didn't put enough money. Amount refunded!")
        return False
    else:
        change = total_input - order_price
        print(f"\nYour order is being prepared! Here is the change: ${round(change)}")
        return True


# TODO: 7. Make coffee using resources and menu
def make_coffee(order, resources):
    """Makes the coffee order from resources available"""
    drink = list(order.keys())
    resources['profit'] += order[drink[0]]['cost']
    ingredients = order[drink[0]]['ingredients']
    resources['water'] -= ingredients['water']
    resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']
    print(f"Here is your {drink[0]}! ☕ Enjoy!")
    return resources


# TODO: 8. main code
def coffee_machine(resources):
    """Runs the coffee machine"""
    # TODO: 2. turn off machine by entering 'OFF'
    order = welcome_text()
    if order == 'report':
        resource_report(resources)
    else:
        check = check_resources(order, resources)
        if not check:
            print("Not enough resources!")
            return
        else:
            money = coin_check(order)
            if money:
                resources = make_coffee(order, resources)
                resource_report(resources)


OFF = False
while not OFF:
    coffee_machine(resources)
    OFF = input("\nPress enter! (For maintenance)").upper()
    if OFF == 'OFF':
        OFF = True
        print("SWITCHED OFF.")
    else:
        OFF = False
