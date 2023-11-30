import ascii

# Menus
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 2.5,
}


# The function allows the technician to add missing materials
def technician():
    more = ""
    while more != "n":
        add = input("\nYou can fill in missing materials for the machine. You can add 100 ml/g at a time.\n"
                    "What material would you like to include? Water, milk, coffee (w/m/c)? ").casefold()
        if add == "w":
            resources['water'] += 100
        if add == "m":
            resources['milk'] += 100
        if add == "c":
            resources['coffee'] += 100
        more = input("\nYour request has been accepted!\n"
                     "Would you like to add more material? (y/n) ").casefold()


# The function checks whether there are sufficient materials for the preparation of espresso
def check_espresso():
    if resources['water'] < menu['espresso']['ingredients']['water']:
        print("There is not enough water in the machine!")
        lack_of_materials = 1
        return lack_of_materials
    if resources['coffee'] < menu['espresso']['ingredients']['coffee']:
        print("There is not enough coffee in the machine!")
        lack_of_materials = 1
        return lack_of_materials


# The function checks whether there are sufficient materials for the preparation of latte
def check_latte():
    if resources['water'] < menu['latte']['ingredients']['water']:
        print("There is not enough water in the machine!")
        lack_of_materials = 1
        return lack_of_materials
    if resources['milk'] < menu['latte']['ingredients']['milk']:
        print("There is not enough milk in the machine!")
        lack_of_materials = 1
        return lack_of_materials
    if resources['coffee'] < menu['latte']['ingredients']['coffee']:
        print("There is not enough coffee in the machine!")
        lack_of_materials = 1
        return lack_of_materials


# The function checks whether there are sufficient materials for the preparation of cappuccino
def check_cappuccino():
    if resources['water'] < menu['cappuccino']['ingredients']['water']:
        print("There is not enough water in the machine!")
        lack_of_materials = 1
        return lack_of_materials
    if resources['milk'] < menu['cappuccino']['ingredients']['milk']:
        print("There is not enough milk in the machine!")
        lack_of_materials = 1
        return lack_of_materials
    if resources['coffee'] < menu['cappuccino']['ingredients']['coffee']:
        print("There is not enough coffee in the machine!")
        lack_of_materials = 1
        return lack_of_materials


# The function coin, checks how many coins were put into the machine and issued a message accordingly.
def price(balance_due, choose):
    print(f"You have to pay {balance_due}$ for {choose}.\n"
          "Please insert coins into the machine.\n"
          "The currencies you can insert are: 'Penni', 'Nickel', 'Dime', 'Quarter'.\n"
          "Please press (p/n/d/q) for each currency.")
    finish = 0
    coins = balance_due
    while finish != 1:
        coins = float("{:.2f}".format(coins))
        more = input(f"\nYou left to pay: {coins}$ insert a coins: and to finish press 'f': ")
        if more == "p":
            coins -= 0.01
        if more == "n":
            coins -= 0.05
        if more == "d":
            coins -= 0.1
        if more == "q":
            coins -= 0.25
        if more == "f":
            finish = 1
    if coins > 0:
        print("\nUnfortunately the coins you put in were not enough, so your money is returned!")
    elif coins < 0:
        extra = abs(coins)
        print(f"\nYou deserve an extra {extra}$, you can take the extra from the machine!")
        finish = 0
    else:
        finish = 0
    return finish


# The function reduces products and adds coins after purchasing espresso
def drinking_espresso():
    resources['water'] -= 50
    resources['coffee'] -= 18
    resources['money'] += 1.5


# The function reduces products and adds coins after purchasing latte
def drinking_latte():
    resources['water'] -= 200
    resources['milk'] -= 150
    resources['coffee'] -= 24
    resources['money'] += 2.5


# The function reduces products and adds coins after purchasing cappuccino
def drinking_cappuccino():
    resources['water'] -= 250
    resources['milk'] -= 100
    resources['coffee'] -= 24
    resources['money'] += 3


# The function declares the acquisition success
def success(choose):
    print(f"\nYour {choose} is ready! Please take it out of the machine!\n{ascii.coffee_ready}")