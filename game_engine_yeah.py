#game engin yeah
from turtle import*

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

class sprite():
    def __init__(self,dat:list,x=0,y=0,visi=True,rot=0):
        
        
        self.x = x
        self.y = y
        self.rot = rot #rotation
        self.data = dat[::-1]
        self.visi=visi #if visible
        self.wi = len(dat[0])
        self.he = len(dat)
        self.last_pos_x=-1
        self.last_pos_y=-1
        self.last_rot=-1
        self.v_x=0
        self.v_y=0
        
    def v_mov(self,)->None:
        if self.v_x != 0 or self.v_y != 0 :
            self.x += self.v_x
            self.y += self.v_y
            
    def rotate(self, dat: list, rot: int) -> list:
        if rot == 90:
            dat=dat[::-1]

        return dat
       

    def draw(self)->None:

        self.data=self.rotate(self.data,self.rot)
        self.v_mov()
        
        if self.visi == True: #only draw if visible
            for i in range(self.he):
                for c in range(self.wi):
                    img.write(self.x + c, self.y + i, self.data[i][c])
        self.last_pos_x,self.last_pos_y=self.x,self.y 
        self.last_rot=self.rot



def regrid():
    reset()
    img.rese()
    grid()

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



dit=[[1,0,0,1],
    [0,0,0,0],
    [1,0,0,1],
    [0,1,1,0]]


blo = sprite(dit,10,10,True)

tracer(0)

regrid()
blo.draw()
updt()

 
done()
