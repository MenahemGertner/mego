import ascii
import list_word
from learning_words import LearningWords
from messages import Messages
# from file import File
import webbrowser
from datetime import date

num = 0
old_word = 0
new_words = []
counter_num = 1
message = Messages
# file = File
learning = LearningWords


def save_file():
    time = date.today()
    file_v = [num, new_words, old_word, time]
    with open("save_location.txt", mode="w") as file:
        # file.write(file_v)
        for item in file_v:
            file.write(str(item) + "\n")


def open_file():
    with open("save_location.txt", mode="r") as file:
        # file_v = file.read()
        file_v = []
        for line in file:
            file_v.append(line.strip())
    return file_v


def applying_file(file_y):
    num_y = int(file_y[0])
    new_words_y = eval(file_y[1])
    old_word_y = int(file_y[2])
    old_time_y = file_y[3]
    new_time_y = date.today()
    return num_y, new_words_y, old_word_y, old_time_y, new_time_y


# Opening text
print(f"\n{ascii.opening}")
run = input("\nFeeling ready? Press Enter to begin!"
            "\nIf you want to reset the program and start from the beginning press 'r': ")
if run == "r":
    print(f"\n\n{ascii.welcome}")

elif run == "":
    print(f"\n{ascii.welcome_back}")
    file_x = open_file()
    num, new_words, old_word, old_time, new_time = applying_file(file_x)
    if old_time != str(new_time) and old_word > 0:
        old_word, new_words = learning.old_words_repetition(new_words)

# A loop to go through all the words in the list one by one
for i in range(num, len(list_word.words)):
    save_file()
    message.progress_message(i)
    while True:
        if not learning.ask_know(num, LearningWords):
            old_word, new_words = learning.ask_know(old_word, num, list_word.words[i], new_words)
            break
        elif learning.ask_know == "s":
            Messages.statistic()
            break
    counter_num = message.success_message(old_word, counter_num)
    num += 1

# End of the program
if old_word != 0:
    print("amm.. you're almost done with the program.. come back tomorrow to repeat your last words..")
else:
    print("Well done!! You have successfully learned all the words!!!!👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼")
