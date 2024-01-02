import list_word
from learning_words import LearningWords

num = 0

a = input("enter y/n ")
if a == "y":
    learn = LearningWords(list_word.words, num)
else:
    learn = LearningWords(list_word.high_tech, num)

for i in range(num, len(learn.location_word())):
    learn.new_word(i)



