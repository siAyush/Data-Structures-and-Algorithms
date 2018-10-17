"""
TST --> Ternary Search Tree
"""


class Node():
    def __init__(self,character):
        self.character = character
        self.left = None
        self.right = None
        self.middle = None
        self.value = 0


class TST():
    def __init__(self):
        self.root = None

    def insert(self,key,value):
        self.root = self.insert_node(self.root,key,value,0)

    def insert_node(self,node,key,value,index):
        c = key[index]

        if node is None:
            node = Node(c)
        if c < node.character:
            node.left = self.insert_node(node.left,key,value,index)
        elif c > node.character:
            node.right = self.insert_node(node.right,key,value,index)
        elif index < len(key)-1:
            node.middle = self.insert_node(node.middle,key,value,index+1)
        else:
            node.value = value
        return node

    def get(self,key):
        node = self.get_node(self.root,key,0)
        if node is None:
            return -1
        return node.value

    def get_node(self,node,key,index):
        if node is None:
            return None
        c = key[index]
        if c < node.character:
            return self.get_node(node.left,key,index)
        elif c > node.character:
            return self.get_node(node.right,key,index)
        elif index < len(key)-1:
            return self.get_node(node.middle,key,index+1)
        else:
            return node
