import turtle as t
import random


t.speed(1000)
t.pendown

length = 10


def sqare():
    for i in range(length//2):
        t.fd(length)
        t.right(90)
        t.fd(1)
        t.right(90)
        t.fd(length)
        t.left(90)
        t.fd(1)
        t.left(90)




for i in range(100):
    dir = random.randint(0,3)
    t.penup()

    match dir:
        case 0:
            t.sety(t.ycor() + 2*length)

        case 1:
            t.sety(t.ycor() + length)
            t.setx(t.xcor() + length)

        case 2:
            pass

        case 3:
            t.sety(t.ycor() + length)
            t.setx(t.xcor() - length)

    t.pendown()

    sqare()
            




t.done()
