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
        self.wants_focus = True
        

    def A_tick(self):
        super().A_tick()
        if self.A_state%4==0:
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            t.teleport(self.x + (self.cursor_pos * self.font_size) + 2,self.y+2)
            t.seth(90)
            t.pendown()
            t.color(100,0,0)
            #t.fd(self.height-4)
            t.fd(10)
            t.color(0,0,0)
            t.penup()

        if not self.has_focus:
            self.wants_A_tick=False


    def onkey(self, key: str):
        super().onkey(key)

        if key == "Left":
            if self.cursor_pos > 0:
                self.cursor_pos-=1

        elif key=="Right":
            if self.cursor_pos < len(self.text)+1:
                self.cursor_pos -= 1
        elif key=="BackSpace":
            if self.cursor_pos > 0:
                self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos+1:]
                self.cursor_pos -= 1
                
        else:
            self.text = self.text[:self.cursor_pos]+key+self.text[self.cursor_pos:]
            self.cursor_pos += 1

        self.mdirty()
