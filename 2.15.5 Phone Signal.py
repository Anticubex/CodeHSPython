speed(0)

for i in range (10,51,10):
    pendown()
    left(90)
    forward(i)
    right(90)
    forward(10)
    right(90)
    forward(i)
    right(90)
    forward(10)
    right(180)
    penup()
    forward(25)
    print(i)
