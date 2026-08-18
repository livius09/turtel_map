import turtle as t
from Node import Node

class scene():
    __Nodes:list[Node]=[]
    
    def __init__(self) -> None:
        self.dirty:bool = True

    def mdirty(self):
        self.dirty=True

    def mclean(self):
        self.dirty=False

    def add_node(self,newNode:Node):
        newNode.set_dirty_callback(self.mdirty)
        self.__Nodes.append(newNode)

    def remove_node(self,oldNode:Node):
        self.__Nodes.remove(oldNode)

    def get_Nodes(self)->list[Node]:
        return self.__Nodes