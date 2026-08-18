import turtle as t
import Node

class lable(Node.Node):
    text:str=""
    font:str="Arial"
    font_size:int = 8

    def __init__(self,txt="") -> None:
        super().__init__()
        self.set_outline(False)
        self.set_text(txt)
        
    def set_text(self,txt:str):
        self.text=txt
        self.width = len(txt)*self.font_size
        self.height = self.font_size+4
        self.mdirty()

    def set_font_size(self, size:int):
        self.font_size = size
        self.width = (len(self.text)*self.font_size)
        self.height = (self.font_size+10)
        self.mdirty()

    
    def render_self(self):
        super().render_self()
        t.teleport(self.x+2,self.y-1)
        t.write(arg=self.text,font=(self.font,self.font_size,"normal"), align="left", move=False)
