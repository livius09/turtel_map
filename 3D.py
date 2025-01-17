from mimetypes import init
from re import X
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
id=0
rendlist=[]



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

def grid()->None:
    penup()
    setheading(0)
    for c in range(img.he+1):
        goto(0,c*10)
        pendown()
        forward(img.wi*10)
        penup()
    setheading(-90)
    for i in range(img.wi+1):
        goto(i*10,img.he*10)
        pendown()
        forward(img.he*10)
        penup()


class vertex():
    def __init__(self,x:int,y:int,conections:tuple) -> None:
        global id,rendlist
        self.id=id
        id+=1
        rendlist.append(self)
        self.x=x
        self.y=y
        self.conection=conections

    def draw(self):
        square(self.x,self.y)

    def draw_line(self):
        for conn_id in self.conection:
            conn_vertex = rendlist[conn_id]
            penup()
            goto(self.x * 10 + 5, self.y * 10 + 5)  # Start from center of square
            pendown()
            goto(conn_vertex.x * 10 + 5, conn_vertex.y * 10 + 5)  # Go to center of connected square
            penup()

b0=vertex(0,0,(1,0))
b1=vertex(10,0,(0,2))
b2=vertex(10,10,(1,2))
b3=vertex(0,10,(0,2))
b4=vertex(15,15,(2,4))
b5=vertex(15,5,(1,4))
b6=vertex(5,15,(3,4))
b7=vertex(5,5,(0,6,7,5))


for obj in rendlist:   
    obj.draw()
    obj.draw_line()


done()
