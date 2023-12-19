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


# a = {3, 2, "l", 4, 44, 5, 44, "j", "asdfgh"}
# a.add(6)
# a.add("hjk")
# print(a)
# b = {}
# if a != b:
#     print(9)
# # כתיבת משתנים לקובץ
# my_list = [1, 2, 3, 4]
# with open("my_file.txt", mode="w") as file:
#     for item in my_list:
#         file.write(str(item) + "\n")
#
# # קריאת משתנים מהקובץ
# with open("my_file.txt", mode="r") as file:
#     my_list = []
#     for line in file:
#         my_list.append(int(line.strip()))
#     print(my_list)

# class Kettle(object):
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False
#
#
# kenwood = Kettle("Kenwood", 8.99)
# # print(kenwood.make)
# # print(kenwood.price)
#
# kenwood.price = 12.75
# # print(kenwood.price)
#
# hamilton = Kettle("Hamilton", 14.55)
# print(hamilton.on)
#
# print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price,
#                                         hamilton.make, hamilton.price))


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# c = Circle(5)
# print(f"The area of the circle with radius {c.radius} is {c.area():.2f}")

# import datetime
# import pytz
#
#
# class Account:
#
#     @staticmethod
#     def _current_time():
#         utc_time = datetime.datetime.utcnow()
#         return pytz.utc.localize(utc_time)
#
#     ''' Simple account class with balance '''
#
#     def __init__(self, name, balance):
#         self._name = name
#         self.__balance = balance
#         self.transaction_list = []
#         print("Account created for " + self._name)
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
#             self.transaction_list.append((self._current_time(), amount))
#             self.transaction_list.append((Account._current_time(), amount))
#
#     def withdraw(self, amount):
#         if self.__balance >= amount:  # to avoid being a millionaire...
#             self.__balance -= amount
#             self.transaction_list.append((Account._current_time(), -amount))
#         else:
#             print("The amount must be <= than the current balance, which is: {}".format(self.__balance))
#
#     def show_balance(self):
#         print("Balance is: {}".format(self.__balance))
#
#     def show_transactions(self):
#         for date, amount in self.transaction_list:
#             if amount > 0:
#                 tran_type = "deposited"
#             else:
#                 tran_type = "withdrawn"
#                 amount *= -1
#             print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))
#
#
# chaim = Account("Chaim", 100)
# chaim.deposit(100)
# chaim.withdraw(200)
# chaim.show_transactions()
# chaim.show_balance()
# # Function Signature -> name + parameter list + ret. val.
# # Code Duplications
# # DRY = Don't Repeat Yourself
# # Static Methods (/functions)
# # non-public (ksheyesh undersdcore mitahat lamishtane)
# # Mangling
# shmuel = Account("Shmuel", 800)
# shmuel.deposit(100)
# shmuel.withdraw(200)
# shmuel.show_transactions()
# shmuel.show_balance()
#
# shmuel.__balance = 300
#
# shmuel._Account__balance = 300
#
# shmuel.show_balance()
# print(shmuel.__dict__)


# class Song:
#     def __init__(self, title, artist, duration=0):
#         self.title = title
#         self.artist = artist
#         self.duration = duration
#
#     def get_title(self):
#         return self.title
#
#     name = property(get_title)
#
#
# s = Song(title="dance", artist="moshes")
# print(s.name)

from player import Player

tim = Player("Tim")

tim.level = 6
tim.level -= 2
tim.level += 1
print(tim)

