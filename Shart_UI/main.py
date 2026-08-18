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
                self.render()
                t.listen()
                sleep(0.2)
        except:
            t.bye()
        


    def render(self):
        if self.cur_scene and self.cur_scene.dirty:
            t.reset()
            self.render_outline()
            for node in self.cur_scene.get_Nodes():
                node.render_self()

            self.cur_scene.mclean()

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

    #figures out wich element was clicked on
    def onclick(self, x:float,y:float):
        if self.cur_scene is not None:
            for node in self.cur_scene.get_Nodes():
                if x > node.x and x < (node.x + node.width):
                    if y > node.y and y < (node.y + node.height):
                        if node.onClick_func:
                            node.onClick_func()




