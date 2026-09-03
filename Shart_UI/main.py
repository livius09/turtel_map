import turtle as t
from time import sleep
from scene import scene
from Node import Node

class app():
    cur_scene:scene|None = None

    
    def __init__(self) -> None:
        t.tracer(0)
        t.hideturtle()
        t.onscreenclick(self.onclick)
        self.bind_leters()
        t.onkeypress(self.on_tab, 'Tab')
        t.onkeypress(self.on_enter, "Return")
        t.colormode(255)
        


    def set_scene(self,new_scene:scene):
        self.cur_scene = new_scene
        self.cur_scene.mdirty()

    def Main_loop(self):
        #register clicks and other events
        #render
        #wait
        #yeah
        try:
            while True:
                self.tick_A()
                self.render()
                t.listen()
                sleep(0.2)
        except:
            t.bye()
        


    def render(self):
        t.hideturtle()
        if self.cur_scene and self.cur_scene.dirty:
            t.reset()
            self.render_outline()
            for node in self.cur_scene.get_Nodes():
                node.render_self()

            self.cur_scene.mclean()

        #needs to be here cause its between the reset and update
        self.tick_A()
        t.hideturtle()

        t.update()
        t.hideturtle()

        

    def render_outline(self):
        t.teleport(0,0)
        t.setheading(0)
        t.pendown()

        for i in range(2):
            t.fd(200)
            t.lt(90)
            t.fd(300)
            t.lt(90)

        t.penup()


    def tick_A(self):
        if self.cur_scene:
            for node in self.cur_scene.get_Animation():
                if node.wants_A_tick:
                    node.A_tick()
                    self.cur_scene.mdirty()
                else:
                    node.A_state=0
                    self.cur_scene.remove_Animation(node)




    #figures out wich element was clicked on
    def onclick(self, x:float,y:float):
        if self.cur_scene:
            for node in self.cur_scene.get_Nodes():
                if x > node.x and x < (node.x + node.width):
                    if y > node.y and y < (node.y + node.height):
                        node.onclick(x,y)
                        if node.wants_A_tick:
                            self.cur_scene.add_Animation(node)

                        if node.wants_focus:
                            self.cur_scene.focused = node
                            node.has_focus = True

    def on_tab(self):
        if self.cur_scene:
            while(len(self.cur_scene.get_Nodes()) > (self.cur_scene.focus_pos % len(self.cur_scene.get_Nodes()))):
                tmp_node = self.cur_scene.get_Nodes()[(self.cur_scene.focus_pos % len(self.cur_scene.get_Nodes()))]

                if (tmp_node.can_be_focused):
                    if self.cur_scene.focused:
                        self.cur_scene.focused.has_focus = False
                
                    tmp_node.has_focus = True
                    self.cur_scene.focused = tmp_node

                    self.cur_scene.mdirty()

                    self.cur_scene.focus_pos+=1
                    break

                self.cur_scene.focus_pos+=1

    def on_enter(self):
        if self.cur_scene:            
            if self.cur_scene.focused:
                tmp_nod = self.cur_scene.focused
                tmp_nod.onclick(tmp_nod.x, tmp_nod.y)
                if tmp_nod.wants_A_tick:
                    self.cur_scene.add_Animation(tmp_nod)

    def bind_leters(self):
        keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"Escape","Left","Right","BackSpace"]
        for key in keys:
            t.onkeypress(lambda k=key:self.handleKey(k),key)

    def handleKey(self,key:str):
        if key=="Escape":
            t.bye()

        if self.cur_scene:
            if self.cur_scene.focused:
                self.cur_scene.focused.onkey(key)


