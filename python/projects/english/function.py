from datetime import date


class File:
    def __init__(self, num, new_words, old_word, time, file, file_y, file_v):
        self.num = num
        self.new_words = new_words
        self.old_word = old_word
        self.time = time
        self.file = file
        self.file_y = file_y
        self.file_v = file_v

    def save_file(self):
        self.file_v = [self.num, self.new_words, self.old_word, self.time]
        with open("save_location.txt", mode="w") as self.file:
            for item in self.file_v:
                self.file.write(str(item) + "\n")

    def open_file(self):
        with open("save_location.txt", mode="r") as self.file:
            self.file_v = []
            for line in self.file:
                self.file_v.append(line.strip())
        return self.file_v

    def applying_file(self):
        num_y = int(self.file_y[0])
        new_words_y = eval(self.file_y[1])
        old_word_y = int(self.file_y[2])
        old_time_y = self.file_y[3]
        new_time_y = date.today()
        return num_y, new_words_y, old_word_y, old_time_y, new_time_y
