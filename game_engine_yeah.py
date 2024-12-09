#game engin yeah
from turtle import*
from time import sleep
import copy

class matrix():
    def __init__(self,he=40,wi=40):
        self.he=he+1
        self.wi=wi+1
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


img=matrix(20,30)

sprites=[] #render pipeline


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

def check(duti:list)->bool: #cheks the integrety of the duti returns true if good and false if its bad

    for i in range(len(duti)):#check if all are a list 
        if not isinstance(duti[i],list):
            print("first")
            return False
            

    whidth = len(duti[0])   
    height = len(duti) 

    for c in range(len(duti)): #check if all colums are the same length
        if len(duti[c])!=whidth:
            print("second")
            return False
        
    

    for g in range(height):#check for every element in the arr if its eitheer a list whit exatly a lenght of 3 of a bolean
        for j in range(whidth):
            if not ((isinstance(duti[g][j],list) and  len(duti[g][j])==3) or isinstance(duti[g][j],bool)) :
                return False
            
    for i in range(height):#check for every in the arr if its a sub arr and if its content are int int the byte range
        for j in range(whidth):
            if isinstance(duti[i][j],list):
                for l in range(3):
                    if not isinstance(duti[i][j][l], int) or not (0 <= duti[i][j][l] <= 255):
                        return False
                    if isinstance(duti[i][j][l], bool):
                        return False
                  
    return True
                
                

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
        
        self.x = x #like well the cur pos
        self.y = y
        self.rot = rot #rotation
        self.data = copy.deepcopy(dat[::-1]) #the visual data in form of a 2d arr /deep coppy so every obj gets its own arr
        self.visi=visi #if visible
        self.wi = len(dat[0])
        self.he = len(dat)
        self.last_pos_x=-1
        self.last_pos_y=-1
        self.last_rot=-1
        self.v_x=0
        self.v_y=0
        self.edgeB=True #if the sprite will bounce from walls or kill itself
        sprites.append(self) #append this sprite to the render pipeline
        
    def v_mov(self,)->None: #moves the sprite by its cur vecs 
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
                sprites.remove(self)  # Remove from the global list #suicide yai
                return
            

        for i in range(self.he):#pretty shitty colision func 
            for j in range(self.wi):
                if self.data[i][j] == 1 and img.read(new_x + j, new_y + i) == 1:
                    self.v_x*= -1 #you cant negate something that is zero
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
        
        if self.visi == True: #only do draw if visible
            for i in range(self.he):
                for c in range(self.wi):
                    img.write(self.x + c, self.y + i, self.data[i][c])
        self.last_pos_x,self.last_pos_y=self.x,self.y 
        self.last_rot=self.rot

def shader(dat:list,shader:list,over=True)->list: #wanabe U V shader
    def wraping(x:int,y:int,arr:list)->list: #aplies the shader repetetly oder so, so no no exeptions
        
        y=y % len(arr)
        x=x % len(arr[y])

        return arr[y][x]

    if over: #if it should overwrite already colored blocks
        for i in range(len(dat)):
            for k in range(len(dat[i])):
                if (dat[i][k]==True or isinstance(dat[i][k],list)):
                    dat[i][k]=wraping(k,i,shader)
    else:
        for i in range(len(dat)):
            for k in range(len(dat[i])):
                if(isinstance(dat[i][k],bool) and dat[i][k]==True):
                    dat[i][k]=wraping(k,i,shader)
    
    return dat

def unshader(dat:list)->list:
    for i in range(len(dat)):
            for k in range(len(dat[i])):
                if isinstance(dat[i][k],list):
                    dat[i][k]=True
    return dat
    



def regrid(): #retset and redraw grid
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


dit=[[False,True,False],
     [False,True,False],
     [False,True,False],
     [True,True,True]]

shad=[[[100,0,0]],
      [[0,100,0]]]

shed=[[[0,100,200]],
      [[100,0,50]]]

print(check(dit))

ik = sprite(dit,15,15)
blo = sprite(dit,10,10)
ik.v_y=-1
ik.v_x=1

blo.data=shader(blo.data,shed,False)

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
    sleep(0.5)
 
done()