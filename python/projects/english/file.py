# class File:
#     def save_file():
#         time = date.today()
#         file_v = [num, new_words, old_word, time]
#         with open("save_location.txt", mode="w") as file:
#             # file.write(file_v)
#             for item in file_v:
#                 file.write(str(item) + "\n")
#
#
#     def open_file():
#         with open("save_location.txt", mode="r") as file:
#             # file_v = file.read()
#             file_v = []
#             for line in file:
#                 file_v.append(line.strip())
#         return file_v
#
#
#     def applying_file(file_y):
#         num_y = int(file_y[0])
#         new_words_y = eval(file_y[1])
#         old_word_y = int(file_y[2])
#         old_time_y = file_y[3]
#         new_time_y = date.today()
#         return num_y, new_words_y, old_word_y, old_time_y, new_time_y


class Car:
 def __init__(self, model):
  self.model = model

 def say_hello(self):
  return "Hello, I'm a {}".format(self.model)


class SportsCar(Car):
 def __init__(self, model, sports_engine):
  super().__init__(model)
  self.sports_engine = sports_engine

 def over_drive(self):
  return "Smashing it!! With my {} engine".format(self.sports_engine)


sportsCar1 = SportsCar('Audi', 'V8')
print(sportsCar1.say_hello())
print(sportsCar1.over_drive())