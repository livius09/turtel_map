import turtle as t
from Node import Node
import math

class checkbox(Node):
    is_ticked:bool=False
    

    def __init__(self):
        super().__init__()
        self.outline=True
        self.width=10
        self.height=10

    def onclick(self,x,y):
        super().onclick(x,y)
        self.is_ticked= not self.is_ticked
        self.mdirty()

    def set_scale(self,new_scale:float):
        num = round(10*new_scale)

        self.width=num
        self.height=num
        self.mdirty()

    def render_self(self):
        super().render_self()

        if self.is_ticked:
            dia = math.sqrt(self.width**2 + self.height**2)
            t.teleport(self.x,self.y)
            t.seth(45)
            t.pendown()
            t.forward(dia)
            t.teleport(self.x, self.y+self.height)
            t.seth(315)
            t.forward(dia)

            t.seth(0)
            t.penup()




