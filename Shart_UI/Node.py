import turtle as t

class Node:
    x:int=0
    y:int=0
    height:int=0
    width:int=0
    outline :bool = False
    color:tuple = (0,0,0)

    wants_A_tick:bool=False
    A_state:int = 0


    dirty_callback = None

    onClick_func = None

    def __init__(self):
        self.mdirty()
        

    def __init_all__(self,x,y,h,w) -> None:
        self.set_x(x)
        self.set_y(y)
        self.set_Width(w)
        self.set_Height(h)
        self.mdirty()

    #mark dirty means it needs to be redrawn as 
    #some things have changed like position
    def mdirty(self):
        if self.dirty_callback:
            self.dirty_callback()

    def set_dirty_callback(self, new_dirty_callback):
        self.dirty_callback = new_dirty_callback

    def set_x(self, x:int ):
        self.mdirty()
        self.x = x

    def set_y(self, y:int ):
        self.mdirty()
        self.y = y

    def set_xy(self,x:int,y:int):
        self.x = x
        self.y = y
        self.mdirty()

    def set_Height(self, Height:int ):
        self.mdirty()
        self.height = Height

    def set_Width(self, Width:int ):
        self.mdirty()
        self.width = Width

    def set_outline(self,state:bool):
        self.mdirty()
        self.outline = state

    def render_self(self):
        if self.outline:
            self.render_outline()

    def set_onclick(self, new_onclick):
        self.onClick_func = new_onclick

    def onclick(self):
        if self.onClick_func:
            self.onClick_func()

    def A_tick(self):
        self.A_state+=1


    def render_outline(self):
        t.teleport(self.x,self.y)
        t.setheading(0)
        t.pendown()

        for i in range(2):
            t.fd(self.width)
            t.lt(90)
            t.fd(self.height)
            t.lt(90)

        t.penup()

