MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def show_report(resources, money):
    '''takes in resources and money. returns printed report.'''
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]


    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"${money}")
    return

def choose_drink(MENU, order):
    '''takes in drink order. returns specific drink dictionary.'''
    drink = MENU[order]
    return drink
    
def payment():
    '''asks how many coins user inputs. calculates & returns the total'''
    print("Please insert coins.")
    quarters = int(input("how many quarters? ")) * 0.25
    dimes = int(input("how many dimes? ")) * 0.10
    nickels = int(input("how many nickels? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def resources_sufficient(drink, resources):
    '''takes in the user_order and the amount of resources. returns True or False if the resources are sufficient'''
    for key in drink["ingredients"]:
        if drink["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False

    return True


def payment_sufficient(total_payment, drink):
    if drink["cost"] > total_payment:
        return False
    else:
        return True

def make_coffee(drink, resources):
    print(f"Here is your {order}. Enjoy!")
    new_resources = {}
    new_resources["water"] = resources["water"] - drink["ingredients"]["water"]
    new_resources["milk"] = resources["milk"] - drink["ingredients"]["milk"]
    new_resources["coffee"] = resources["coffee"] - drink["ingredients"]["coffee"]
    return new_resources

# def coffee_machine(order, resources, MENU, money):
#     if order == "report":
#         show_report(resources, money)
#     else:
#         drink = choose_drink(MENU, order)
#         total_payment = payment()
#         if resources_sufficient(drink, resources):
#             if payment_sufficient(total_payment, drink):
#                 money += drink["cost"]
#                 change = round(total_payment - drink["cost"], 2)
#                 print(f"Here is ${change} in change.")
#                 new_resources = make_coffee(drink, resources)
#                 return new_resources
#             else:
#                 return resources
#         else:
#             return resources



should_continue = True

while should_continue:

    # order = input("What would you like? (espresso/latte/cappuccino): ")
    # new_resources = coffee_machine(order, resources, MENU, money)
    # resources = new_resources

    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        show_report(resources, money)
    elif order == "off":
        should_continue = False
    else:
        drink = choose_drink(MENU, order)
        total_payment = payment()
        if resources_sufficient(drink, resources):
            if payment_sufficient(total_payment, drink):
                money += drink["cost"]
                change = round(total_payment - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                resources = make_coffee(drink, resources)
            else:
                print("Sorry that's not enough money. Money refunded.")









