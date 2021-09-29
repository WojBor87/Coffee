from data import MENU, resources


def check_resources(drink) -> bool:
    """
    Function check is there enough resources to make drink user choose
    :param drink: Drink which user choose (espresso/latte/cappuccino
    :return: True or False depends if there is enough resources inside
    """
    got_resources = True
    for check in resources:
        if drink[check] > resources[check]:
            got_resources = False
            print(f"Not enough {check} in Coffee Machine")
    return got_resources


def check_transaction(amount, cost):
    if amount == cost:
        return True
    elif amount > cost:
        rest = round(amount - cost, 3)
        print(f"rest:$ {rest}")
        return True
    else:
        return False


def process_coins(drink):
    quarters = int(input("How much quarters do you pay? ")) * 0.25
    dimes = int(input("How much dimes do you pay? ")) * 0.10
    nickles = int(input("How much nickles do you pay? ")) * 0.05
    pennies = int(input("How much pennies do you pay? ")) * 0.01
    amount_paid = quarters + dimes + nickles + pennies
    return check_transaction(amount_paid, drink)


def make_coffee(drink):
    for current_resource in resources:
        if drink[current_resource]:
            resources[current_resource] -= drink[current_resource]


next_coffee = True

while next_coffee:
    choose = ""
    while choose not in ["resources", "fill", "off", "espresso", "latte", "cappuccino"]:
        choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose == "resources":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    elif choose == "fill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    elif choose == "off":
        next_coffee = False
    else:
        if check_resources(MENU[choose]["ingredients"]):
            if process_coins(MENU[choose]["cost"]):
                make_coffee(MENU[choose]["ingredients"])
                print(f"Here you are, here is your {choose}")
            else:
                print("Not enough coins")
        else:
            print("Need to refill Coffee Machine!")
