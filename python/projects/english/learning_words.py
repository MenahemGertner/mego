import webbrowser


class LearningWords:

    def __init__(self, words_list, number):
        self.words_list = words_list
        self.number = number

    def location_word(self):
        return self.words_list

    def new_word(self, index):
        self.number += 1
        print(f"\nYour new word is:\n\n{self.number}. '{self.words_list[index]}'")
        knowing = input("\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
        if knowing == "n":
            self.chak_translation(self.words_list[index])

    def chak_translation(self, current_word):
        chak = input("Write the word and you can get its translation: ")
        while True:
            if chak.casefold() == current_word.casefold():
                break
            else:
                chak = input("Spell the word correctly again: ")
        webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={current_word}%0A&op=translate")
