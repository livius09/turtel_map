
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
    def __init__(self,dat:list,x=0,y=0,visi=True,rot=0,he=3,wi=3,weight=1,bounc=1):
        
        if len(dat) != he*wi:
            raise ValueError("Data lengt does not match sprite dimensions")
        
        self.x = x
        self.y = y
        self.rot = rot #rotation
        self.dat = dat
        self.visi=visi #if visible
        self.wi = wi #whidt
        self.he = he #heigt
        self.last_pos_x=-1
        self.last_pos_y=-1
        self.last_rot=-1    

        self.weight = weight
        self.v_x=0
        self.v_y=0
        self.bounc=bounc
        self.gravi=1

    def bounce(self):
        if self.x <= 0 or self.x >= img.wi - self.wi:
            self.v_x*= -1
        if self.y<=0 or self.y >= img.he - self.he:
            self.v_y*= -1

    def gravity(self):
        self.v_y-=self.gravi

    def v_mov(self,)->None:
        if self.v_x != 0 or self.v_y != 0 :
            self.x += self.v_x
            self.y += self.v_y
            self.x = max(0, min(self.x, img.wi - self.wi))
            self.y = max(0, min(self.y, img.he - self.he))

    def rphysik(self):
        self.bounce()
        self.gravity()
        self.v_mov()

         
        

            
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

        self.rphysik()
        
        if self.visi == True: #only draw if visible
            for i in range(self.he):
                for c in range(self.wi):
                    img.write(self.x + c, self.y + i, self.dat[i*self.he + c])
        self.last_pos_x,self.last_pos_y=self.x,self.y 
        self.last_rot=self.rot

            

dit=[1,1,1,
     0,1,0,
     0,1,0]

def regrid():
    reset()
    img.rese()
    grid()

blo = sprite(dit,20,20,)
blo.v_x=1 

tracer(0)
while(True):
    regrid()
    blo.draw()
    updt()
    update()
    sleep(0.2)


 
done()
