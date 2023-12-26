class Messages:
    @staticmethod
    def progress_message(num_now):
        if num_now > 0 and num_now % 20 == 0:
            print(f"👏🏼👏🏼👏🏼 You already know '{num_now}' words from the list!!! 👏🏼👏🏼👏🏼")

    @staticmethod
    def success_message(old_num):
        if old_num > 0 and old_num % 5 == 0:
            print(f"👏🏼👏🏼👏🏼 Wow!! Today you already learned '{old_num}' new words!!! 👏🏼👏🏼👏🏼")

    @staticmethod
    def statistic(old_words_num, num):
        words_left = 1000 - num
        percentage = round((num - old_words_num) / 10)
        print(f"\n               statistics"
              f"\n-------------------------------------------"
              f"\n Words you have already learned: {num}"
              f"\n Words still left: {words_left}"
              f"\n Percentage of words you already know: {percentage}%"
              f"\n New words you learned today: {old_words_num}"
              f"\n-------------------------------------------\n")

