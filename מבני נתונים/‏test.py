# exercise 1
def count_number(first, num):
    counter = 0
    while first != None:
        if num == first.get_value():
            counter += 1
        first = first.get_next()
    return counter


# exercise 2
def avg(first):
    counter = 0
    total = 0
    while first != None:
        counter += 1
        total += first.get_value()
        first = first.get_next()
    average = total / counter
    return average


# exercise 3
def max_index(first):
    location = 0
    while first != None:
        location += 1
        first = first.get_next()
    return location


# exercise 4
def first_index_num(first, num):
    location = 0
    while first != None:
        location += 1
        if num == first.get_value():
            return location
        first = first.get_next()


# exercise 5
def last_index(first, num):
    location = 0
    last_location = 0
    while first != None:
        location += 1
        if num == first.get_value():
            last_location = location
        first = first.get_next()
    return last_location


# exercise 6
def add_ten(first):
    while first != None:
        first.set_value(first.get_value() + 10)
        first = first.get_next()


# exercise 7
def div_two(first):
    while first != None:
        first.set_value(first.get_value() / 2)
        first = first.get_next()


# exercise 8
def add_val(first, val):
    while first != None:
        first.set_value(first.get_value() + val)
        first = first.get_next()


# exercise 9
def check_update_val(first, val):
    while first != None:
        if first.get_value() >= val:
            first.set_value(first.get_value() * 2)
        else:
            first.set_value(first.get_value() / 2)
        first = first.get_next()



