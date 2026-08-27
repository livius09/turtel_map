import turtle as t
from lable import lable

class Textfield(lable):
    cursor_pos:int=0
    cursor_visible=False

    def __init__(self, ) -> None:
        super().__init__("")
        self.width = 40
        self.outline = True
        self.can_be_focused = True

    def onclick(self, x: float, y: float):
        super().onclick(x, y)
        self.wants_A_tick = True
        

    def A_tick(self):
        super().A_tick()
        if self.A_state%4==0:
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            t.teleport(self.x + (self.cursor_pos * self.font_size) + 2,self.y+2)
            t.seth(0)
            t.pendown()
            t.fd(self.height-4)
            t.penup()


    def onkey(self, key: str):
        super().onkey(key)
        self.text += key
        self.cursor_pos += 1



    
