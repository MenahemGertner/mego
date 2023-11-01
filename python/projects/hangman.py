import ascii
import random

# Variables
colors = ['red', 'black', 'gold', 'green', 'purple', 'orange', 'brown', 'yellow']
word = random.choice(colors)
word_2 = list(word)
word_3 = ["_"] * len(word)
count = -1
win = 0
winner = len(word)
game_over = 7
hang = 0

# start
start = input(f"{ascii.welcome}\n\nIf you are ready press Enter!")
if start == "":
    print("\nYou must find the hidden letters and discover the chosen color!\n")

    # letter selection
    while win != 1:
        print(f"\nYou have {game_over} more attempts left\n\n{word_3}\n")
        letter = input("Please choose a letter: ")
        count = -1
        for i in word_2:
            count += 1

            # success
            if i == letter:
                word_3[count] = letter
                word_2[count] = []
                winner -= 1
                if winner == 0:
                    win = 1
                break

            # failure
            elif count == len(word_2) - 1:
                print(ascii.hangman[hang])
                hang += 1
                game_over -= 1

                # game over
                if game_over == 0:
                    print(f"{ascii.game_over}\nThe correct word was: '{word}'")
                    exit()

    # win
    print(ascii.win)
