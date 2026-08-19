import turtle as t
from lable import lable

class Button(lable):
    def __init__(self, txt="") -> None:
        super().__init__(txt)
        self.outline = True

    def onclick(self):
        super().onclick()
        self.wants_A_tick = True

    def A_tick(self):
        super().A_tick()
        
        if self.A_state<2:
            self.render_ofset(1)
        elif self.A_state<3:
            self.render_ofset(2)
        elif self.A_state<4:
            self.render_ofset(3)
        elif self.A_state<6:
            self.render_ofset(2)
        else:
            self.wants_A_tick = False

            

    def render_ofset(self,ofs:int):
        t.teleport(self.x-ofs,self.y-ofs)

        t.setheading(0)
        t.pendown()

        for i in range(2):
            t.fd(self.width+2*ofs)
            t.lt(90)
            t.fd(self.height+2*ofs)
            t.lt(90)

        t.penup()
    