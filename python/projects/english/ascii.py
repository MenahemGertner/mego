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


import  random


def uppercase(letter_list):
    big_letter = []
    new_list = []
    for i in letter_list:
        if 91 > ord(i) > 64:
            big_letter.append(i)
    for i in range(len(letter_list)):
        random.shuffle(big_letter)
        new_list.append(big_letter[0])
    print(''.join(new_list))


uppercase(input("Enter a string.. "))
