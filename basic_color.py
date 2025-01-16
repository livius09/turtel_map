from turtle import*
from time import sleep
from random import choice


class matrix():
    def __init__(self,he=40,wi=40):
        self.he=he
        self.wi=wi
        self.size=self.he*self.wi
        self.arr=[[0 for x in range(self.wi)] for y in range(self.he)]
    
    def read(self,x: int,y: int)-> any:
        x,y=int(x),int(y)
        return (self.arr[x][y])
    
    def write(self,x: int,y: int,w:any)->None:
        x,y=int(x),int(y)
        self.arr[x][y]=w
        
    def rese(self):
        self.arr=[[0 for x in range(self.wi)] for y in range(self.he)]


img=matrix()



def square(x: int, y: int, RGB: list = None) -> None:
    penup()
    goto(x * 10, y * 10)
    if RGB is not None:
        color(RGB[0] / 255, RGB[1] / 255, RGB[2] / 255)
    else:
        color(0, 0, 0)
    pendown()
    setheading(0)
    begin_fill()
    for i in range(4):
        forward(10)
        right(-90)
    end_fill()
    color(0, 0, 0)
    penup()


def updt():
    for i in range(img.he):
        for c in range(img.wi):
            val=img.read(i,c)
            if isinstance(val,list):
                rgb = img.read(i,c)
                square(i,c,rgb)
            elif img.read(i,c) == 1:
                square(i,c)
