#turtel_map
from turtle import*
from time import sleep
import random


class matrix():
    def __init__(self,he=40,wi=40):
        self.he=he
        self.wi=wi
        self.size=self.he*self.wi
        self.arr=[False,]*self.size
    
    def read(self,x: int,y: int)-> bool:
        x,y=int(x),int(y)
        adr= x+(y * self.wi)
        return (self.arr[adr])
    
    def write(self,x: int,y: int,w:bool)->None:
        x,y=int(x),int(y)
        adr= x+(y* self.wi)
        self.arr[adr]=w
        
    def rese(self):
        self.arr=[0]*self.size


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

def diagram(ar:list)->None:
    if len(ar) > img.wi:
        OverflowError
    penup()
    for i in range(len(ar)):
        for c in range(ar[i]):
            img.write(i,c,True)

def markers()->None:
    
    def mark():
        pendown()
        forward(10)
        right(90)
        forward(5)
        right(180)
        forward(10)
        right(180)
        forward(5)
        left(90)
        penup()


    goto(0,0)
    setheading(0)
    for i in range (img.wi):
        mark()

    goto(0,0)
    setheading(90)
    for i in range (img.he):
        mark()

def normal_distrubution()->list:
    n=[]
    for i in range(600):
        n.append(random.randint(0,20)+random.randint(0,20))
    o=[0,]*img.wi
    for c in range(img.wi): 
        o[c]= n.count(c)

    return(o)


tracer(0)
markers()
diagram(normal_distrubution())
updt()
update()
done()

