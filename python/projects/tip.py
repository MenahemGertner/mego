size = input("What size pizza would you like? (large/medium/small): ")
pepperoni = input("Would you like extra pepperoni on your pizza? (Yes/No): ")
olive = input("Would you like extra mushrooms and olives on the pizza? (Yes/No): ")
cheese = input("Would you like extra cheese on your pizza? (Yes/No): ")
price = 0

if size == "large":
    price += 25
    if pepperoni == "yes":
        price += 6
    if olive == "yes":
        price += 5
elif size == "medium":
    price += 20
    if pepperoni == "yes":
        price += 4
    if olive == "yes":
        price += 5
else:
    price += 15
    if pepperoni == "yes":
        price += 2
    if olive == "yes":
        price += 3
if cheese == "yes":
    price += 3
print(f"\ntotal payment: {price}")