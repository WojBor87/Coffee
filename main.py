from data import MENU, resources


def check_resources(drink) -> bool:
    """
    Function check is there enough resources to make drink user choose
    :param drink: Drink which user choose (espresso/latte/cappuccino
    :return: True or False depends if there is enough resources inside
    """
    got_resources = True
    for check in drink:
        if drink[check] > resources[check]:
            got_resources = False
            print(f"Not enough {check} in Coffee Machine")
    return got_resources


def check_transaction(amount, cost):
    if amount == cost:
        resources["money"] += cost
        return True
    elif amount > cost:
        rest = round(amount - cost, 3)
        print(f"Here is :${rest} in change.")
        resources["money"] += cost
        return True
    else:
        return False


def process_coins():
    amount_paid = int(input("How much quarters do you pay? ")) * 0.25
    amount_paid += int(input("How much dimes do you pay? ")) * 0.10
    amount_paid += int(input("How much nickles do you pay? ")) * 0.05
    amount_paid += int(input("How much pennies do you pay? ")) * 0.01
    return amount_paid


def make_coffee(drink):
    for current_resource in drink:
        if drink[current_resource]:
            resources[current_resource] -= drink[current_resource]


is_online = True
resources["money"] = 0

while is_online:
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
        is_online = False
    else:
        if check_resources(MENU[choose]["ingredients"]):
            total_paid = process_coins()
            if check_transaction(total_paid, MENU[choose]["cost"]):
                make_coffee(MENU[choose]["ingredients"])
                print(f"Here you are, here is your {choose}")
            else:
                print(f"Sorry that's not enough money. {total_paid} refunded.")
        else:
            print("Need to refill Coffee Machine!")
