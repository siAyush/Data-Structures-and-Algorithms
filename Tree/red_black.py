# Node Colors
Black = 'Black'
Red = 'Red'

class Node():
    def __init__(self,data,parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.color = Red          # default color is red


class Red_Black():
    def __init__(self):
        self.root = None

    def in_order_traverse(self):
        if self.root:
            self._in_order_traverse(self.root)

    def _in_order_traverse(self,node):
        if node.left:
            self._in_order_traverse(node.left)
        print('Node data %s Node color %s'%(node.data ,node.color))
        if node.right:
            self._in_order_traverse(node.right)

    def parent(self,node):        # return the parent of node
        return node.parent

    def set_black(self,node):    # change the default color of node
        node.color = Black

    def uncle(self,node):
        if node:
            if self.parent(node):
                parent = self.parent(node)
            if self.parent(node) == None:
                parent = None
            if parent is not None:
                grand_parent = self.parent(parent)
            if parent == None:
                grand_parent = None
            if parent and grand_parent is not None:
                if parent.data < grand_parent.data:
                    return grand_parent.right
                if parent.data > grand_parent.data:
                    return grand_parent.left
        return None

    def insert(self,data):
        if not self.root:
            self.root = Node(data,None)
            self.set_black(self.root)
        self._insertNode(data,self.root)

    def _insertNode(self,data,node):
        if data < node.data:
            if node.left:
                self._insertNode(data,node.left)
            else:
                node.left = Node(data,node)
                node = node.left
        if data > node.data:
            if node.right:
                self._insertNode(data,node.right)
            else:
                node.right = Node(data,node)
                node = node.right
        return self.violation(data,node)

    def violation(self,data,node):
        uncle = self.uncle(node)
        parent = self.parent(node)
        if parent is None:
            grand_parent = None
        if parent:
            grand_parent = self.parent(parent)

        # Case I (when uncle and node is red)
        if node and grand_parent:
            if node.data < grand_parent.data and grand_parent.parent == None and uncle.color == Red:
                self.set_black(grand_parent)
                self.set_black(grand_parent.left)
                self.set_black(grand_parent.right)
                return grand_parent

            elif node.data < grand_parent.data and uncle.color == Red:
                grand_parent.color = Red
                self.set_black(grand_parent.left)
                self.set_black(grand_parent.right)
                return grand_parent

        # Case II (when uncle is black)

a = Red_Black()
a.insert(10)
a.insert(5)
a.insert(15)
a.insert(11)
a.in_order_traverse()
