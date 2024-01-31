class IntNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def value_to_string(self):
        return self.value


# exercise 5
num = 2
first = None
for i in range(4, 0, -1):
    first = IntNode(i, first)
temp = first
counter = 0
while temp != None:
    if num == temp.get_value():
        counter += 1
    temp = temp.get_next()
print(counter)

# exercise 6
first = None
for i in range(4, 0, -1):
    first = IntNode(i, first)
temp = first
counter = 0
total = 0
while temp != None:
    counter += 1
    total += temp.get_value()
    temp = temp.get_next()
average = total / counter
print(average)

