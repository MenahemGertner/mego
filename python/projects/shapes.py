import random

password = []
letters = ['a', 'b', 'c']
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
password.append(random.choice(letters))
print(f"Before\n{password}")
random.shuffle(password)
print(f"\nAfter\n{password}")


