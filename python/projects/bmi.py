age = int(input("What is your age? (years) "))
weight = float(input("What is your weight?? (kg) "))
height = float(input("What is your height?? (meter) "))
BMI = round(weight / height ** 2, 1)
if age <= 65:
    if BMI < 18.5:
        print(f"\nYour BMI is: {BMI} And you are underweight!")
    elif 18.5 <= BMI <= 24.9:
        print(f"\nYour BMI is: {BMI} And you are at a normal weight")
    elif BMI > 30:
        print(f"\nYour BMI is: {BMI} And you are obese!!")
    else:
        print(f"\nYour BMI is: {BMI} And you are overweight!")
elif 65 < age <= 74:
    if BMI < 22:
        print(f"\nYour BMI is: {BMI} And you are underweight!")
    elif 22 <= BMI <= 26.9:
        print(f"\nYour BMI is: {BMI} And you are at a normal weight")
    elif BMI > 30:
        print(f"\nYour BMI is: {BMI} And you are obese!!")
    else:
        print(f"\nYour BMI is: {BMI} And you are overweight!")
else:
    if BMI < 23:
        print(f"\nYour BMI is: {BMI} And you are underweight!")
    elif 23 <= BMI <= 27.9:
        print(f"\nYour BMI is: {BMI} And you are at a normal weight")
    elif BMI > 30:
        print(f"\nYour BMI is: {BMI} And you are obese!!")
    else:
        print(f"\nYour BMI is: {BMI} And you are overweight!")