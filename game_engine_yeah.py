#game engin yeah
from turtle import*
from time import sleep

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
sprites=[]


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
        self.edgeB=True
        sprites.append(self)
        
    def v_mov(self,)->None:
        new_x = self.x + self.v_x
        new_y = self.y + self.v_y

        if self.edgeB:
            if new_x < 0 or new_x + self.wi > img.wi: 
                self.v_x*= -1
                new_x=self.x + self.v_x

            if new_y < 0 or new_y + self.he > img.he:
                self.v_y*=-1
                new_y = self.y + self.v_y
        else:
            if new_x < 0 or new_x + self.wi > img.wi or new_y < 0 or new_y + self.he > img.he:
                sprites.remove(self)  # Remove from the global list
                return
            




        for i in range(self.he):
            for j in range(self.wi):
                if self.data[i][j] == 1 and img.read(new_x + j, new_y + i) == 1:
                    self.v_x*= -1
                    self.v_y*= -1
                    return

        self.x = new_x
        self.y = new_y    
            
            
    def rotate(self,rot:int) -> list:
                if rot==180:
                    tmp=self.data[::-1]
                elif rot==90:
                    tmp =[[0 for x in range(self.he)] for y in range(self.wi)]
                    for i in range(self.he):
                        for j in range(self.wi):
                            tmp[j][i]=self.data[i][j]     
                    self.data=tmp[::-1]
            
            

       

    def draw(self)->None:
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



dit=[[1,1,1],
     [0,1,0],
     [0,1,1]]


ik = sprite(dit,15,15)
blo = sprite(dit,10,10)
ik.v_y=-1
ik.v_x=1

blo.v_y=1
blo.v_x=1
blo.edgeB=False

tracer(0)

while True:
    regrid()    

    for obj in sprites:
        obj.draw()

    updt()
    update()
    sleep(0.2)
 
done()
