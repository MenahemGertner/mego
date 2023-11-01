import os
user = 0
hi_proposal = 0
hi_name = ""

while user != 1:
    name = input("Enter a name: ")
    proposal = int(input("Enter a your proposal: "))
    if proposal > hi_proposal:
        hi_proposal = proposal
        hi_name = name
    back = input("Would you like to enter another contestant? (y/n) ")
    if back == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        break
print(f"The highest bid was given by: '{hi_name}' in the amount of '{hi_proposal}' NIS")