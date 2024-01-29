opening = '''                /|  /|  ---------------------------
                ||__||  |         Learning         |
               /   O O\__         English          |
              /          \        Easily!!         |
             /      \     \                        |
            /   _    \     \ ----------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \C_c_c_c'''

welcome = '''  (¯`·.¸¸.·´¯`·.¸¸.·´¯)
  ( \                 / )
 ( \ )               ( / )
( ) (    Welcome!!    ) ( )
 ( / )               ( \ )
  ( /                 \ )
   (_.·´¯`·.¸¸.·´¯`·.¸_)'''

welcome_back = '''  (¯`·.¸¸.·´¯`·.¸¸.·´¯)
  ( \                 / )
 ( \ )               ( / )
( ) (  Welcome back!! ) ( )
 ( / )               ( \ )
  ( /                 \ )
   (_.·´¯`·.¸¸.·´¯`·.¸_)'''

remote = '''           ⇓ After learning the meaning of the word ⇓
 -----------------------------------------------------------------
| Read the last words in English and its interpretation in Hebrew |
|    and vice versa, read in Hebrew and translate to English!     |
 -----------------------------------------------------------------'''



def elaborate_number(num1):
    num2 = num1 - 1
    counter = 0
    while num2 > 0:
        if num1 % num2 == 0:
            counter += num2
        num2 -= 1
    if num1 == counter:
        print(num1)
        return True

def check_elaborate(num):
    count = 1
    while num != 0:
        if elaborate_number(count):
            num -= 1
        count += 1

check_elaborate(int(input("Enter a number: ")))
