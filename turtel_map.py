#turtel_map
from turtle import*
from time import sleep
from random import choice


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

def setrandom():
    for i in range(img.he):
        for c in range(img.wi):
            img.write(i,c,choice([True,False]))

def life() -> None:
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    new_img = matrix(img.he, img.wi)
    
    for i in range(img.he):
        for c in range(img.wi):
            u = 0   
            for dx, dy in neighbors:
                ni, nc = i + dx, c + dy
                if 0 <= ni < img.he and 0 <= nc < img.wi:
                    if img.read(ni, nc):
                        u += 1
            
            if img.read(i, c):  
                if u < 2 or u > 3:
                    new_img.write(i, c, False) 
                else:
                    new_img.write(i, c, True)
            else:
                if u == 3:
                    new_img.write(i, c, True) 
                else:
                    new_img.write(i, c, False)
    
    img.arr = new_img.arr

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

    
while input("end ?: ") != "yes":
    img.write(input("x: "),input("y: "),True)


while True:
    
    tracer(0)
    reset()
    grid()
    life()
    updt()
    update()
    sleep(0.5)



done()