from datas import MENU, resources


# Coins
penny = 0.01
dime = 0.1
nickel = 0.05
quarter = 0.25

payment_request = "You need to pay before receiving it"
price = 0
total = 0


def resource():
    for i in resources:
        print(resources[i])


def cost(_type):
    global price
    price = MENU[_type]['cost']
    print(f"The price of this is: {MENU[_type]['cost']}")
    return price


def payment():
    global total
    _penny = int(input("Penny: "))
    _dime = int(input("Dime: "))
    _nickel = int(input("Nickel: "))
    _quarter = int(input("Quarter: "))
    total = (_penny * penny) + (_dime * dime) + (_nickel * nickel) + (_quarter * quarter)
    return total


def statistics(_type):
    ingredient = MENU[_type]["ingredients"]
    for i in ingredient:
        resources[i] = resources[i] - ingredient[i]


_continue = True
while _continue:
    type_coffee = input("What would you like? ").lower()
    if type_coffee == "report":
        resource()
    elif type_coffee == "espresso":
        cost(type_coffee)
        print(payment_request)
        payment()
        if total == price:
            print("Thank you. Bon appetite!")
            statistics(type_coffee)
            _continue = True
