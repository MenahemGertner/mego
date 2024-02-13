class Pab:
    def __init__(self, drink_name, ingredients, alcohol_percentage, price):
        self.__drink_name = drink_name
        self.__ingredients = ingredients
        if 0 <= alcohol_percentage <= 100:
            self.__alcohol_percentage = alcohol_percentage
        else:
            print("Invalid value entered!")
        self.__price = price

    def get_drink_name(self):
        return self.__drink_name

    def set_drink_name(self, name):
        self.__drink_name = name

    def get_ingredients(self):
        return self.__ingredients

    def set_ingredients(self, ingre):
        self.__ingredients = ingre

    def get_alcohol_percentage(self):
        return self.__alcohol_percentage

    def set_alcohol_percentage(self, drink):
        if 0 <= drink <= 100:
            self.__alcohol_percentage = drink
        else:
            print("Invalid value entered!")

    def get_price(self):
        return self.__price

    def set_price(self, cost):
        self.__price = cost

    def display(self):
        print(f"name: {self.__drink_name},\n ingredients: {self.__ingredients}, \nalcohol: {self.__alcohol_percentage}, \nprice: {self.__price}")


drink1 = Pab('bir',  'barely, water', 777, 10)
drink2 = Pab('wine', 'grapes', 13, 100)


def mor_alcohol(dri1, dri2):
    if dri1.get_alcohol_percentage() > dri2.get_alcohol_percentage():
        dri1.display()
    else:
        dri2.display()


def annoying_customer(drink):
    drink.set_price(drink.get_price() * 1.05)


def ingredients_print(drink):
    ingredient = drink.get_ingredients()
    for ing in ingredient.split(','):
        print(ing)

print(drink2.display())