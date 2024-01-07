class Messages:
    def __init__(self):
        self.counter = 1

    def progress_message(self, numbers):
        if numbers > 0 and numbers % 20 == 0:
            print(f"👏🏼👏🏼👏🏼 You already know '{numbers}' words from the list!!! 👏🏼👏🏼👏🏼")

    def success_message(self, old_num):
        if old_num > self.counter:
            self.counter = old_num
        if self.counter % 5 == 0:
            print(f"👏🏼👏🏼👏🏼 Wow!! Today you already learned '{old_num}' new words!!! 👏🏼👏🏼👏🏼")
            self.counter += 1

    def statistic(self, old_num, numbers):
        words_left = 1000 - numbers
        percentage = round((numbers - old_num) / 10)
        print(f"\n               statistics"
              f"\n-------------------------------------------"
              f"\n Words you have already learned: {numbers}"
              f"\n Words still left: {words_left}"
              f"\n Percentage of words you already know: {percentage}%"
              f"\n New words you learned today: {old_num}"
              f"\n-------------------------------------------\n")
