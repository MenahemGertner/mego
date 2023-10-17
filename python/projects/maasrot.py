import math
a = 1
b = 0
while a != 0:
    a = float(input("Enter your income: "))
    b += a
n = input("\nAre you interested in giving homes or maaser? If homesh press h, if maaser press m ")
if n == "h":
    print("\nYour homesh is: ", b / 5, "and in a circle upwards: ", math.ceil(b / 5))
else:
    print("\nYour maasrot is: ", b / 10, "and in a circle upwards: ", math.ceil(b / 10))

