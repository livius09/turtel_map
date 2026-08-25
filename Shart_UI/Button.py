import turtle as t
from lable import lable

class Button(lable):
    def __init__(self, txt="") -> None:
        super().__init__(txt)
        self.outline = True
        self.can_be_focused = True

    def onclick(self,x,y):
        super().onclick(x,y)
        self.wants_A_tick = True

    def A_tick(self):
        super().A_tick()

        t.color()
        
        if self.A_state<2:
            self.render_ofset(1)
        elif self.A_state<3:
            self.render_ofset(2)
        elif self.A_state<4:
            self.render_ofset(4)
        elif self.A_state<6:
            self.render_ofset(2)
        else:
            self.wants_A_tick = False
    