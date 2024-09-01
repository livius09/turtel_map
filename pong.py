
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

def updt():
    for i in range(img.he):
        for c in range(img.wi):
            if img.read(i,c) == True:
                square(i,c)

class sprite():
    def __init__(self,dat:list,x=0,y=0,rot=0,he=3,wi=3,visi=True):
        if len(dat) != he*wi:
            raise ValueError("Data lengt does not match sprite dimensions")
        
        self.x = x
        self.y = y
        self.rot = rot
        self.dat = dat#[::-1]
        self.visi=visi
        self.wi = wi
        self.he = he
        self.last_pos_x=-1
        self.last_pos_y=-1
        self.last_rot=-1
        self.v_x=0
        self.v_y=0

    def v_mov(self,):
        if self.v_x != 0 or self.v_y != 0 :
            self.x += self.v_x
            self.y += self.v_y

    def rotate(self, dat: list, rot: int) -> list:
        grid = [dat[i*self.wi:(i+1)*self.wi] for i in range(self.he)]

        if rot == 0:
            return dat  # No change
        elif rot == 90:
            return [grid[self.he-1-j][i] for i in range(self.wi) for j in range(self.he)]
        elif rot == 180:
            return dat[::-1]  # Flip the entire list
        elif rot == 270:
            return [grid[j][self.wi-1-i] for i in range(self.wi) for j in range(self.he)]
        else:
            raise ValueError("Rotation has to be either 0, 90, 180, or 270 degrees.")

    def draw(self,)->None:

        self.dat=self.rotate(self.dat,self.rot)
        self.v_mov()

        if self.visi == True:
            for i in range(self.he):
                for c in range(self.wi):
                    img.write(self.x + c, self.y + i, self.dat[i*self.he + c])
        self.last_pos_x,self.last_pos_y=self.x,self.y
        self.last_rot=self.rot

def regrid():
    reset()
    img.rese()
    grid()
            

bdat=[1,1,
     1,1]

pdat=[1,0,0,0,0,0,0,
      1,0,0,0,0,0,0,
      1,0,0,0,0,0,0,
      1,0,0,0,0,0,0,
      1,0,0,0,0,0,0,
      1,0,0,0,0,0,0,
      1,0,0,0,0,0,0]


ball = sprite(bdat,20,20,0,2,2)
pa1= sprite(pdat,1,18,0,7,7)


tracer(0)
while True:
    regrid()
    pa1.draw()
    ball.draw()
    updt()
    ball.x += 1
    update()
    sleep(1)

 
done()
