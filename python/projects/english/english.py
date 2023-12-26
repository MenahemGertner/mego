import ascii
import list_word
import function
import webbrowser
from datetime import date

num = 0
old_word = 0
new_words = []
counter_num = 0


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


def statistic(old_words_num):
    words_left = 1000 - num
    percentage = round((num - old_words_num) / 10)
    print(f"\n               statistics"
          f"\n-------------------------------------------"
          f"\n Words you have already learned: {num}"
          f"\n Words still left: {words_left}"
          f"\n Percentage of words you already know: {percentage}%"
          f"\n New words you learned today: {old_words_num}"
          f"\n-------------------------------------------\n")


def new_word(number, the_word):
    print(f"\nYour new word is:\n\n{number + 1}. '{the_word}'")
    knowing = input("\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
    return knowing


def ask_know(old_word_list, number, list_wo, new_wo):
    while True:
        knows = new_word(number, list_wo)
        if knows == "":
            print("\nGreat!\n")
            break
        elif knows == "s".casefold():
            statistic(old_word_list)
        else:
            # Creating a list of the unfamiliar words for repetition and memorization
            new_wo.append(list_wo)
            old_word_list += 1
            # Instructions for memorizing the new words
            chak_translation(list_wo)
            memorization(old_word_list, new_wo)
            break
    return old_word_list, new_wo


def old_words_repetition(new_words_list):
    print(f"\n\n\nFirst, we'll go over the old words you had trouble with,"
          f"\nand then we'll go back to the list again to continue with the new words.")
    index = 0
    memorize = []
    for j, word in enumerate(new_words_list):
        index, memorize = ask_know(index, j, word, memorize)
    print("\n\nExcellent! Now we will return to the list!\n")
    return index, memorize


def chak_translation(current_word):
    chak = input("Write the word and you can get its translation: ")
    while True:
        if chak.casefold() == current_word.casefold():
            break
        else:
            chak = input("Spell the word correctly again: ")
    webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={current_word}%0A&op=translate")


def memorization(old_words, new_words_list):
    print(f"___________________________________________________________\n\n\n\n\n\n\n\n\n\n{ascii.remote}"
          f"\n\n\nThe last words: >>>>>----------------------->   '{', '.join(new_words_list[-3:])}'")
    if old_words >= 7:
        print("And also the old word: >>>>----------------->   '" + new_words_list[-7] + "'")

    print(f"\n\n           If you forgot the meaning of one of the words,"
          f"\nyou can write it down here and get its translation, Otherwise press Enter"
          f"\n      ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓")
    free_chak_translation(old_words)
    print("\nExcellent! Now that you have memorized the word well, you can move on to the next word!")


def free_chak_translation(old_words_list):
    translate = input()
    while True:
        if translate == "":
            break
        elif translate == "s".casefold():
            statistic(old_words_list)
        else:
            webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={translate}%0A&op=translate")
        translate = input("You can check another word again. If you wish to continue press Enter ")


# A message of encouragement after 20 words from the list
def progress_message(num_now):
    if num_now > 0 and num_now % 20 == 0:
        print(f"👏🏼👏🏼👏🏼 You already know '{num_now}' words from the list!!! 👏🏼👏🏼👏🏼")


# A message of encouragement after learning 5 new words
def success_message(old_num, counter):
    if old_num > counter:
        counter = old_num
    if counter % 5 == 0:
        print(f"👏🏼👏🏼👏🏼 Wow!! Today you already learned '{old_num}' new words!!! 👏🏼👏🏼👏🏼")
        counter += 1
        return counter


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
        old_word, new_words = old_words_repetition(new_words)

# A loop to go through all the words in the list one by one
for i in range(num, len(list_word.words)):
    save_file()
    progress_message(i)
    old_word, new_words = ask_know(old_word, num, list_word.words[i], new_words)
    counter_num = success_message(old_word, counter_num)

    num += 1

# End of the program
if old_word != 0:
    print("amm.. you're almost done with the program.. come back tomorrow to repeat your last words..")
else:
    print("Well done!! You have successfully learned all the words!!!!👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼")
