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


def process_coins():
    amount_paid = 0
    return amount_paid


def check_transaction(amount):
    paid_enough = False
    return paid_enough


def make_coffee(drink):
    for current_resource in resources:
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
        got_enough_resources = check_resources(MENU[choose]["ingredients"])
        if got_enough_resources:
            paid = process_coins()
            if check_transaction(paid):
                make_coffee(MENU[choose]["ingredients"])
            else:
                pass
        else:
            print("Need to refill Coffee Machine!")

    # TODO 5. Process coins.
    # TODO 6. Check transaction successful?
    # TODO 7. Make Coffee.
