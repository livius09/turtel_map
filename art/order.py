import turtle
import random
import math

opions = [0, 45, 90, 135, 180, 225, 270, 315]
even = [0, 90,180, 270]
turtle.speed(100)
turtle.pendown

length=10

angle_length = math.sqrt(2*length)

for i in range(1000):
    num = random.randint(0,len(opions)-1)
    turtle.setheading(opions[num])

    if opions[num] in even:
        turtle.forward(length)
    else:
        turtle.forward(angle_length)

turtle.done()