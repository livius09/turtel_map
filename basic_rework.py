from turtle import*
from time import sleep
from random import choice


class matrix():
    def __init__(self,he=40,wi=40):
        self.he=he
        self.wi=wi
        self.size=self.he*self.wi
        self.arr=[[0 for x in range(self.wi)] for y in range(self.he)]
    
    def read(self,x: int,y: int)-> bool:
        x,y=int(x),int(y)
        return (self.arr[x][y])
    
    def write(self,x: int,y: int,w:bool)->None:
        x,y=int(x),int(y)
        self.arr[x][y]=w
        
    def rese(self):
        self.arr=[[0 for x in range(self.wi)] for y in range(self.he)]


img=matrix()


def square(x: int,y: int) ->None :
    penup()
    goto(x*10,y*10)
    pendown()
    setheading(0)
    begin_fill()
    for i in range(4):
        forward(10)
        right(-90)
    end_fill()
    penup()

def updt():
    for i in range(img.he):
        for c in range(img.wi):
            if img.read(i,c) == True:
                square(i,c)

