from main import app
from scene import scene
from lable import lable

myapp = app()

frontscene = scene()
mylb = lable("helo world")
mylb.set_xy(20,20)
mylb.set_outline(True)

mylb.onClick_func = lambda : print("Hello world")

frontscene.add_node(mylb)



seclb = lable("move")
seclb.set_xy(40,40)
seclb.set_outline(True)

seclb.onClick_func = lambda : seclb.set_x(seclb.x+5)

frontscene.add_node(seclb)


myapp.set_scene(frontscene)

myapp.Main_loop()

