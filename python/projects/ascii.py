# import datetime as td
#
#
# def say_hello(name):
#     time = td.datetime.today()
#     print(f"hello {name}! The time now is: {time.hour}:{time.minute} you left 1 minute!")
#     begin = time.minute
#     return begin
#
#
# def time_now():
#     real_time = td.datetime.today()
#     b = real_time.minute
#     condition(b)
#
#
# def condition(a):
#     if a >= beginning:
#         print("You lost the time!")
#         exit()
#
#
# beginning = say_hello(input("Enter your name: ")) + 1
# while True:
#     time_now()
#
#
#
#
#
# # euro_prices = [100, 120, 140, 180, 220, 240]
#
#
# # def convert(price, coin_type):
# #     rates = {'USD': 3.52, 'CAD': 2.5, 'EUR': 3.78}
# #     rate = rates[coin_type]
# #     return round(price * rate, 2)
# #
# #
# # nis_prices = [convert(i, 'EUR')for i in euro_prices]
# # print(nis_prices)
# # for i in nis_prices:
# #     print(i)

# angle = 90
# timmy.penup()
# timmy.forward(80)
# timmy.pendown()
# a = 30
# for i in range(50):
#     timmy.pencolor(random.random(), random.random(), random.random())
#     timmy.circle(a, 250, 6)
#     a +=2


# for i in range(8):
#     for j in range(12):
#         timmy.pencolor(random.random(), random.random(), random.random())
#         timmy.circle(20, 345)
#         timmy.forward(10)
#     for j in range(15):
#         timmy.pencolor(random.random(), random.random(), random.random())
#         timmy.circle(20, 345)
#         timmy.forward(1)
# timmy.left(96)
# for i in range(10):
#     timmy.pencolor(random.random(), random.random(), random.random())
#     timmy.circle(angle, 370)
#     timmy.left(90)
#     timmy.forward(3)
#     timmy.right(90)
#     angle -= 3
# for i in range(40):
#     timmy.pencolor(random.random(), random.random(), random.random())
#     timmy.circle(20, 180)
#     timmy.circle(-30, 320)
#     timmy.forward(150)
#     timmy.circle(30, 330)
#     timmy.forward(140)
#
# timmy.penup()
# timmy.forward(400)
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
# screen.listen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_right():
#     tim.right(10)
#
#
# def move_left():
#     tim.left(10)
#
#
# def move_back():
#     tim.back(10)
#
#
# screen.onkey(key="space", fun=move_forwards)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_back)
#
# screen.exitonclick()

# from turtle import Turtle, Screen
# import random
# while True:
#     screen = Screen()
#     screen.setup(width=500, height=400)
#     y_position = -150
#     color_list = ['red', 'yellow', 'brown', 'blue', 'green', 'purple']
#     turtles = []
#
#     for i in range(6):
#         tim = Turtle(shape="turtle")
#         tim.penup()
#         tim.color(color_list[i])
#         tim.goto(x=-230, y=y_position)
#         y_position += 60
#         turtles.append(tim)
#     turtle_choice = screen.textinput(title="Turtle_choice!", prompt="Which turtle will win? (enter a color): ")
#     print(turtle_choice)
#
#     condition = True
#     while condition:
#         for tim in turtles:
#             tim.forward(random.randint(1, 10))
#             if any(tim.xcor() > 220 for tim in turtles):
#                 condition = False
#                 break
#
#     if turtle_choice == tim.color()[0]:
#         play_again = screen.textinput(title="You are the win!", prompt="Do you want play again? (y/n)")
#     else:
#         play_again = screen.textinput(title="You are lose!", prompt="Do you want play again? (y/n)")
#     screen.reset()
#     if play_again == "n":
#         exit()
#
# screen.exitonclick()

# a = "abcdefghijk"
# b = 123456
# print("{1:8} is {0:92}".format(a, b))
# print("%s is %.2f" %(a, b))

# for a, b in enumerate("asdfghjkl"):
#     print(a+1, b)

# class Men:
#     def __init__(self, age, high):
#         self.age = age
#         self.high = high
#         self.feet = 2
#
#
# mens = [{'man1': {'age': 22, 'high': 1.8}}, {'man2': {'age': 28, 'high': 1.7}}, {'man3': {'age': 42, 'high': 1.65}},
#         {'man4': {'age': 19, 'high': 1.75}}, {'man5': {'age': 31, 'high': 1.78}}]
# for index, man in enumerate(mens):
#     a = Men(age=list(man.values())[0]['age'], high=list(man.values())[0]['high'])
#     print(f"Man number {index + 1}. in age: {a.age}, and high: {a.high}, and he has: {a.feet} feet")

# class User:
#     def __init__(self, userID, username):
#         self.id = userID
#         self.username = username
#         # default values
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, whats_his_name):
#         self.following += 1
#         whats_his_name.followers += 1
#
#
# chaim = User("1234", "Chaim")
# ben = User("5678", "Benayahu")
#
# ben.follow(chaim)
# print(ben.following)
# print(chaim.followers)
import xmltodict
import json

xml_text = '''<fruit_story>
    <fruit>
        <name>mango</name>
        <category>fruits</category>
        <season>summer</season>
        <form_of_eating>fresh</form_of_eating>
        <price>3$</price>
    </fruit>
    <fruit>
        <name>Carrot</name>
        <category>vegetables</category>
        <season>all year round</season>
        <form_of_eating>fresh or cooked</form_of_eating>
        <price>1$</price>
    </fruit>
    <fruit>
        <name>eggplant</name>
        <category>vegetables</category>
        <season>all year round</season>
        <form_of_eating>cooked</form_of_eating>
        <price>1.5$</price>
    </fruit>
    <fruit>
        <name>Pomelo</name>
        <category>fruits</category>
        <season>winter</season>
        <form_of_eating>fresh</form_of_eating>
        <price>1.5$</price>
    </fruit>
    <fruit>
        <name>strawberry</name>
        <category>fruits</category>
        <season>summer</season>
        <form_of_eating>fresh</form_of_eating>
        <price>5$</price>
    </fruit>
</fruit_story>'''

json_text = json.dumps(xmltodict.parse(xml_text), indent=4)
print(json_text)
