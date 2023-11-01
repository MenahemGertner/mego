def right():
    for i in range(2):
        move()
        turn_left()
        turn_left()
        turn_left()
        
def left():
    move()
    turn_left()

def loop():
    for i in range(6):
        left()
        right()
        left()
loop()
        




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
