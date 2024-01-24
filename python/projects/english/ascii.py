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


class Coffee:
    def _init_(self, name, kind, strength, price) :
        self.name = name
        self.kind = kind
        self.strength = strength
        self.price = price


def same_product(crr):
    manufacturer_name = crr[0].name
    for i in crr:
        if manufacturer_name != i.name:
            return False
    return True


def weak_sorts(crr, num):
    new_list = []
    for i in crr:
        if i.strength < num:
            new_list.append(i)
    return new_list


def most_expensive(crr):
    hi_price = 0
    for i in crr:
        if i.price > hi_price:
            hi_price = i.price
    return hi_price



