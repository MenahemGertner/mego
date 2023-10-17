import draw
import random

fish = 0
new_fish = 0
steps = 1

# Opening and general description.
# A detailed description appears mainly within the text itself to the user during the program
print(draw.welcome)

# The entrance gate to the swamp
begin = input()
if begin == "":
    print(draw.entrance)
print("You are now entering the area of the swamps,\n"
      "you must now choose from two possible ways,\n"
      "would you like to turn to the right or left side? (r/l)")
input()

# Until now, it was only a small experience in the game, and now a real entry into the game
for i in range(0, 100):  # This loop allows the player to be retrieved to the beginning of the game
    print(f"Oh no!\nYou stepped on a frog!\n"
          f"You must start the route from the beginning!!\n{draw.entrance}\n"
          f"Where would you like to turn to the right or left? (r/l)")
    input()
    steps += 1
    print("Interesting choice!\n"
          "You now have the option to cast your net into the water,\n"
          "would you like to try your luck?\n"
          "Press Enter to cast the net into the water!")

    # Throwing a net into the water to collect fish
    net = input()
    if net == "":
        new_fish += random.randint(1, 5)
        fish += new_fish
        print(f"{new_fish} fish have been added to your basket!\n{draw.fish}\n")

    # Reaching the first real crossroads
    print(f"Now you have two right or left turns.\n{draw.roads}\n"
          "Turning right is full of aquatic animals,\n"
          "you can win fish but also step on a frog and go back.\n"
          "Turning left has no risk but no chance either!\n"
          "what will you choose (r/l)")
    side = input().casefold()
    steps += 1
    if side == "r":
        choose = random.randint(0, 1)
        if choose == 0:
            net = input("Your bet was successful!\npress Enter to cast the net into the water!")
            if net == "":
                new_fish = 5
                fish += new_fish
                print(f"\n{new_fish} fish have been added to your basket!\n{draw.fish}")
        else:
            continue

    # Second crossroads
    for j in range(0, 100):
        steps += 1
        side = input(f"\nYou are now at a crossroads.\n{draw.roads}\n"
                     "On the right side there is a shortcut by jumping over the water,\n"
                     "but if you fall into the water you may be swept back with the water..\n"
                     "turning left is the long way (r/l)").casefold()
        if side == "r":
            choose = random.randint(0, 1)
            if choose == 0:
                print("\nYou successfully jumped over the water!!!\n"
                      "You are now on to the next step!\n")
                break
            else:
                print("\nUnfortunately you are swept away with the water,\n"
                      "and you return to the previous intersection.")
                continue
        else:
            net = input("You now have a chance to cast the net into the water,\n"
                        "press enter to collect fish!")
            if net == "":
                new_fish += random.randint(1, 5)
                fish += new_fish
                print(f"{new_fish} fish have been added to your basket!\n{draw.fish}")

            # Third crossroads
            side = input(f"Now you are facing a crossroads again.\n{draw.roads}\n"
                         f"If you turn right,\n"
                         f"you will reach an area rich in fish and you can collect a lot of fish again,\n{draw.fish}\n"
                         f"but you will risk being hit by a shark that may devour everything you have already "
                         f"collected so far,\n{draw.shark}\n"
                         f"turning left you will skip this area (r/l)").casefold()
            steps += 1
            if side == "r":
                net = input("You now have a chance to cast the net into the water,\n"
                            "press enter to collect fish!")
                if net == "":
                    new_fish += random.randint(6, 15)
                    fish += new_fish
                    print(f"{new_fish} fish have been added to your basket!\n{draw.fish}")
                choose = random.randint(0, 1)
                if choose == 0:
                    fish = 0
                    print("But unfortunately your success is mixed with sadness.\n"
                          "Because a big shark empties all the fish in the net! Don't despair,\n"
                          "try your luck again later!")
        break

    # Fourth crossroads
    side = input(f"\nNow you are standing in front of a waterfall,\n{draw.water_fall}\n"
                 "this is the last chance to collect a lot of fish into the basket,\n"
                 "but also to accidentally step on a frog and return to the beginning of the game.\n"
                 "Would you like to turn right and take the risk? Or step left the safe way out? (r/l)")
    steps += 1
    if side == "r":
        choose = random.randint(0, 1)
        if choose == 0:
            new_fish += random.randint(15, 30)
            fish += new_fish
            print(f"\nYour bet paid off! {new_fish} fish have been added to your basket!\n{draw.fish}")
        else:
            continue
    break

# End of the program
print(f"\nYou managed to get out of the swamp and finish the game successfully!!\n"
      f"You crossed the swamp in {steps} steps!\n"
      f"And in your basket there are {fish} fish!!\n{draw.fish}\n\n"
      f"Enjoyed? You can play again..")
