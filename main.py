import data


def check_resources(drink):
    """
    Function check is there enough resources to make drink user choose
    :param drink: Drink which user choose (espresso/latte/cappuccino
    :return: True or False depends if there is enough resources inside
    """
    got_resources = False
    return got_resources


next_coffee = True

while next_coffee:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choose = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Print report of all coffee machine resources
    if choose == "resources":
        for resource in data.resources:
            print(f"{resource}: {data.resources[resource]}")

    # TODO 3. Turn off the Coffee Machine by entering “off” to the prompt.
    elif choose == "off":
        next_coffee = False

    # TODO 4. Check resources sufficient?
    else:
        got_enough_resources = check_resources(choose)

    # TODO 5. Process coins.
    # TODO 7. Check transaction successful?
    # TODO 8. Make Coffee.
