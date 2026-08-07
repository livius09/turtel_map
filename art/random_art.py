import turtle
import random

opions = [0, 90,180, 270]
turtle.speed(100)
turtle.pendown
for i in range(1000):
    turtle.setheading(random.choice(opions))
    turtle.forward(10)

turtle.done()