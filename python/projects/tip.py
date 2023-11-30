import ascii
import function
import os

new_user = 0

# The opening of the program
while new_user == 0:
    start = input("\nTo start the machine press Enter: ")
    if start == "":
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = input(f"\n{ascii.welcome}\n").casefold()

        # Access to a technician
        if choice == "off":
            code = int(input("Please enter a code: "))
            if code == 1234:
                function.technician()

        # Report generation
        if choice == "report":
            print(function.resources)

        # Espresso selection
        if choice == "espresso":
            check = function.check_espresso()
            if check == 1:
                continue
            left_to_pay = 1.5
            pay = float(function.price(left_to_pay, choice))
            if pay == 1:
                continue
            function.drinking_espresso()
            function.success(choice)

        # Latte selection
        if choice == "latte":
            check = function.check_latte()
            if check == 1:
                continue
            left_to_pay = 2.5
            pay = float(function.price(left_to_pay, choice))
            if pay == 1:
                continue
            function.drinking_latte()
            function.success(choice)

        # Cappuccino selection
        if choice == "cappuccino":
            check = function.check_cappuccino()
            if check == 1:
                continue
            left_to_pay = 3
            pay = float(function.price(left_to_pay, choice))
            if pay == 1:
                continue
            function.drinking_cappuccino()
            function.success(choice)
