#turtel_map
from turtle import*
from time import sleep
from random import choice


class matrix():
    def __init__(self,he=40,wi=40):
        self.he=he
        self.wi=wi
        self.size=self.he*self.wi
        self.arr=[0]*self.size
    
    def read(self,x: int,y: int)-> bool:
        adr= x+(y * self.wi)
        return (self.arr[adr])
    
    def write(self,x: int,y: int,w:bool)->None:
        adr= x+(y* self.wi)
        self.arr[adr]=w
        
    def rese(self):
        self.arr=[0]*self.size


img=matrix()


def square(x: int,y: int) ->None :
    penup()
    goto(x*10,y*10)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

def updt():
    for i in range(img.he):
        for c in range(img.wi):
            if img.read(i,c) == True:
                square(i,c)

def setrandom():
    for i in range(img.he):
        for c in range(img.wi):
            img.write(i,c,choice([True,False]))

while True:
    setrandom()
    tracer(0)
    reset()
    updt()
    update()



done()