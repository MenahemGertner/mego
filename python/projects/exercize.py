# 1
# def entire_number(num1):
#     num2 = num1
#     counter = 0
#     while num2 > 0:
#         counter += num2 % 10
#         num2 //= 10
#     return num1 % counter == 0
#
#
# for i in range(1, 1001):
#     if entire_number(i):
#         print(i)

# 2
# a = [2, 4, 3, 4, 2]
# print(set(a))

# 3
import random


# def is_ordered(arr):
#     odd_list = []
#     even_list = []
#     for ar in arr:
#         if ar % 2 == 0:
#             odd_list.append(ar)
#         else:
#             even_list.append(ar)
#     return arr == odd_list + even_list


# def build_ordered(size, x, y):
#     array = []
#     odd_lis = []
#     even_lis = []
#     for i in range(size):
#         array.append(random.randint(x, y))
#     print(array)
#     if not is_ordered(array):
#         for ar in array:
#             if ar % 2 == 0:
#                 odd_lis.append(ar)
#             else:
#                 even_lis.append(ar)
#         array = odd_lis + even_lis
#     return array
#
# print(build_ordered(20, 20, 25))


# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:
#     print("It is impossible to divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print(f"the answer is: {result}")
# finally:
#     print("End of the program")

# def what1(num):
#     if num == 0:
#         return 1
#     else:
#         return 10 * what1(num//10)
#
#
# print(what1(123))


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list[2:4])
# print(list[1:7:3])
# print(list[4:2])
# print(list[2:4:-1])
# print(list[4:2:-1])
# print(list[::-2])
# print(list[2:-2])


class Coffee:
    b = 0
    def __init__(self, name, kind, strength, price):
        self.name = name
        self.kind = kind
        self.strength = strength
        self.price = price
        Coffee.b += 1

    def get_name(self):
        return self.name

    def get_strength(self):
        return self.strength

    def get_price(self):
        return self.price

    def display(self):
        print(f"name: {self.name}, kind: {self.kind}, strength: {self.strength}, price: {self.price}")


def same_products(crr):
    name = crr[0]
    for cr in crr:
        if cr.get_name() != name.get_name():
            return False
    return True

def weak_sorts(crr, num):
    stran = []
    for cr in crr:
        if cr.get_strength() < num:
            stran.append(cr)
    return stran

def most_expensive(crr):
    expensive = 0
    most_expensive = []
    for cr in crr:
        if cr.get_price() > expensive:
            expensive = cr.get_price()
    for cr in crr:
        if cr.get_price() == expensive:
            most_expensive.append(cr)
    for i in most_expensive:
        i.display()
a = Coffee('ff', 'uy', 55, 44)
print(a.b)
a = Coffee('ff', 'uy', 55, 44)
print(a.b)