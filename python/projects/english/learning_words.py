# class Learning_words:
#     def new_word(number, the_word):
#         print(f"\nYour new word is:\n\n{number + 1}. '{the_word}'")
#         knowing = input("\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
#         return knowing
#
#
#     def ask_know(old_word_list, number, list_wo, new_wo):
#         while True:
#             knows = new_word(number, list_wo)
#             if knows == "":
#                 print("\nGreat!\n")
#                 break
#             elif knows == "s".casefold():
#                 message.statistic(old_word_list, number)
#             else:
#                 # Creating a list of the unfamiliar words for repetition and memorization
#                 new_wo.append(list_wo)
#                 old_word_list += 1
#                 # Instructions for memorizing the new words
#                 chak_translation(list_wo)
#                 memorization(old_word_list, new_wo)
#                 break
#         return old_word_list, new_wo
#
#
#     def old_words_repetition(new_words_list):
#         print(f"\n\n\nFirst, we'll go over the: '{len(new_words_list)}' old words you had trouble with,"
#               f"\nand then we'll go back to the list again to continue with the new words.")
#         index = 0
#         memorize = []
#         for j, word in enumerate(new_words_list):
#             index, memorize = ask_know(index, j, word, memorize)
#         print("\n\nExcellent! Now we will return to the list!\n")
#         return index, memorize
#
#
#     def chak_translation(current_word):
#         chak = input("Write the word and you can get its translation: ")
#         while True:
#             if chak.casefold() == current_word.casefold():
#                 break
#             else:
#                 chak = input("Spell the word correctly again: ")
#         webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={current_word}%0A&op=translate")
#
#
#     def memorization(old_words, new_words_list):
#         print(f"___________________________________________________________\n\n\n\n\n\n\n\n\n\n{ascii.remote}"
#               f"\n\n\nThe last words: >>>>>----------------------->   '{', '.join(new_words_list[-3:])}'")
#         if old_words >= 7:
#             print("And also the old word: >>>>----------------->   '" + new_words_list[-7] + "'")
#
#         print(f"\n\n           If you forgot the meaning of one of the words,"
#               f"\nyou can write it down here and get its translation, Otherwise press Enter"
#               f"\n      ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓")
#         free_chak_translation(old_words)
#         print("\nExcellent! Now that you have memorized the word well, you can move on to the next word!")
#
#
#     def free_chak_translation(old_words_list):
#         translate = input()
#         while True:
#             if translate == "":
#                 break
#             elif translate == "s".casefold():
#                 message.statistic(old_words_list, num)
#             else:
#                 webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={translate}%0A&op=translate")
#             translate = input("You can check another word again. If you wish to continue press Enter ")
from messages import Messages
import webbrowser
import ascii
message = Messages


class LearningWords:
    def __init__(self, words_list):
        self.knowing = None
        self. words_list = words_list
        self.old_word_list = 0
        self.new_wo = []

    def new_word(self, number, the_word):
        print(f"\nYour new word is:\n\n{number + 1}. '{the_word}'")
        self. knowing = input("\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
        if self.knowing == "n":
            return False

    def ask_know(self, number, list_wo):
        while True:
            knows = self.new_word(number, list_wo)
            if knows == "":
                print("\nGreat!\n")
                break
            elif knows == "s".casefold():
                message.statistic(self.old_word_list, number)
            else:
                # Creating a list of the unfamiliar words for repetition and memorization
                self.new_wo.append(list_wo)
                self.old_word_list += 1
                # Instructions for memorizing the new words
                self.chak_translation(list_wo)
                self.memorization(self.old_word_list, self.new_wo)
                break
        return self.old_word_list, self.new_wo

    def old_words_repetition(self, new_words_list):
        print(f"\n\n\nFirst, we'll go over the: '{len(new_words_list)}' old words you had trouble with,"
              f"\nand then we'll go back to the list again to continue with the new words.")
        index = 0
        memorize = []
        for j, word in enumerate(new_words_list):
            index, memorize = self.ask_know(index, j, word, memorize)
        print("\n\nExcellent! Now we will return to the list!\n")
        return index, memorize

    def chak_translation(self, current_word):
        chak = input("Write the word and you can get its translation: ")
        while True:
            if chak.casefold() == current_word.casefold():
                break
            else:
                chak = input("Spell the word correctly again: ")
        webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={current_word}%0A&op=translate")

    def memorization(self, old_words, new_words_list):
        print(f"___________________________________________________________\n\n\n\n\n\n\n\n\n\n{ascii.remote}"
              f"\n\n\nThe last words: >>>>>----------------------->   '{', '.join(new_words_list[-3:])}'")
        if old_words >= 7:
            print("And also the old word: >>>>----------------->   '" + new_words_list[-7] + "'")

        print(f"\n\n           If you forgot the meaning of one of the words,"
              f"\nyou can write it down here and get its translation, Otherwise press Enter"
              f"\n      ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓")
        self.free_chak_translation(old_words)
        print("\nExcellent! Now that you have memorized the word well, you can move on to the next word!")

    def free_chak_translation(self, old_words_list):
        translate = input()
        while True:
            if translate == "":
                break
            elif translate == "s".casefold():
                message.statistic(old_words_list, self.num)
            else:
                webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={translate}%0A&op=translate")
            translate = input("You can check another word again. If you wish to continue press Enter ")
