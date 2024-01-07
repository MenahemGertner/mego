import list_word
import ascii
from learning_words import LearningWords, BackWords
from file import File

num = 0
new_words = []

print(f"\n{ascii.opening}")
run_program = input("\nFeeling ready? Press Enter to continue!"
                    "\nIf you want to reset the program and start from the beginning press 'r': ")
if run_program.casefold() == "r":
    choose_list = input("\nFor the 1,000 most useful words in English write 'w',"
                        "for useful words in high-tech write 'h': ")
    print(f"\n\n{ascii.welcome}")

else:
    print(f"\n{ascii.welcome_back}")
    files = File(number=None, new_words=None, choose=None)
    files.open_file()
    choose_list = files.choose
    new_words = files.new_words
    num = files.number

    if files.old_time != str(files.new_time) and len(files.new_words) > 0:
        learn = BackWords(files.new_words, num, new_words, choose_list)
        learn.new_word()

if choose_list.casefold() == "w":
    learn = LearningWords(list_word.words, num, new_words, choose_list)
elif choose_list.casefold() == "h":
    learn = LearningWords(list_word.high_tech, num, new_words, choose_list)

learn.new_word()

# End of the program
if len(new_words) != 0:
    print("amm.. you're almost done with the program.. come back tomorrow to repeat your last words..")
else:
    print("Well done!! You have successfully learned all the words!!!!👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼")
