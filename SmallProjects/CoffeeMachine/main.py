import MENU as menu
def check_current_resources():
    current_resources = menu.resources
    for key,value in current_resources.items():
        if key == "water":
            print(f"{key}: {value}ml")
        if key == "milk":
            print(f"{key}: {value}ml")
        if key == "coffee":
            print(f"{key}: {value}g")
        if key == "money":
            print(f"{key}: ${value}")
    return
def check_resources_sufficient(drink_name):
    cost = menu.MENU[drink_name]["cost"]
    if drink_name in menu.MENU:
        ingredients_needed = menu.MENU[drink_name]["ingredients"]
        for ingredient, amount in ingredients_needed.items():
            if ingredient in menu.resources:
                if menu.resources[ingredient] >= amount:
                    print(f"Resources are sufficient. Please insert coins ({cost}).")
                    return True
                else:
                    print(f"Sorry, there is not enough {ingredient}.")
                return False
        print(f"Sorry, {ingredient} is not available.")
        return False
    else:
        print(f"{drink_name} is not available in the menu.")
        return False

def process_coins(drink_name):
    cost = menu.MENU[drink_name]["cost"]
    quarters = input("Please insert quarters ($0.25): ")
    quarters_converted = int(quarters) * 0.25
    dimes = input("Please insert dimes ($0.10): ")
    dimes_converted = int(dimes) * 0.1
    nickles = input("Please insert nickles ($0.05): ")
    nickles_converted = int(nickles) * 0.05
    pennies = input("Please insert pennies ($0.01): ")
    pennies_converted = int(pennies) * 0.01
    inserted_money = quarters_converted + dimes_converted + nickles_converted + pennies_converted
    change = inserted_money - cost
    existing_money = menu.resources["money"]
    profit = existing_money + cost
    if inserted_money >= cost:
        print("Transaction succesful. Proceeding...")
        print(f"Your change is ${change}")
        menu.resources["money"] = profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(drink_name):
    if drink_name in menu.MENU:
        ingredients_needed = menu.MENU[drink_name]["ingredients"]
        resource_instock = menu.resources
        for ingredient, value1 in ingredients_needed.items():
            for resource, value2 in resource_instock.items():
                if ingredient == resource:
                    new_resource_value = value2 - value1
                    menu.resources[f"{resource}"] = new_resource_value
                return True



while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino)☕").lower()

    if user_choice == "report":
        check_current_resources()

    if user_choice == "off":
        break

    if user_choice == "espresso":
        drink_name = user_choice
        if check_resources_sufficient(drink_name) is True:
            if process_coins(drink_name) is True:
                if make_coffee(drink_name) is True:
                    print("Coffee ready, please take your drink.")
            else:
                pass
        else:
            pass

    if user_choice == "latte":
        drink_name = user_choice
        if check_resources_sufficient(drink_name) is True:
            if process_coins(drink_name) is True:
                if make_coffee(drink_name) is True:
                    print("Coffee ready, please take your drink.")
            else:
                pass
        else:
            pass

    if user_choice == "cappuccino":
        drink_name = user_choice
        if check_resources_sufficient(drink_name) is True:
            if process_coins(drink_name) is True:
                if make_coffee(drink_name) is True:
                    print("Coffee ready, please take your drink.")
            else:
                pass
        else:
            pass