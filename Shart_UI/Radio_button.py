import turtle as t
from Node import Node
import math

class Radio_Button(Node):
    options:list[str]=[]
    selected:str= ""
    

    def __init__(self):
        super().__init__()

    def add_option(self, option:str):
        self.options.append(option)
        self.width = len(max(self.options, key=len))*8 + 12
        self.height = len(self.options)*16
        self.mdirty()

    def render_self(self):
        super().render_self()
        

        for i in range(len(self.options)):
            
            t.teleport(self.x+4,self.y+4+i*12)
            t.setheading(0)
            t.pendown()
    
            for k in range(4):
                t.fd(10)
                t.lt(90)

            if self.options[i]==self.selected:
                dia = math.sqrt(2*(10**2))
                t.teleport(self.x+4,self.y+4+i*12)
                t.seth(45)
                t.pendown()
                t.forward(dia)
                t.teleport(self.x+4,self.y+4+i*12+10)
                t.seth(315)
                t.forward(dia)
    
                t.seth(0)

            t.teleport(self.x+18,self.y+4+i*12)
            t.write(self.options[i])

            
    
            t.penup()

    def onclick(self, x: float, y: float):
        super().onclick(x, y)
        y_relative = y-self.y

        #idk dawg