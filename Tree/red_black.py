# Node Colors
Black = 'Black'
Red = 'Red'

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
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
        print('Node data %s'%node.data)
        if node.right:
            self._in_order_traverse(node.right)

    def parent(self,node):       # return the parent of node
        return node.parent

    def set_black(self,node):    # change the default color of node
        node.color = Black

    def uncle(self,node):
        parent = self.parent(node)
        grand_parent = self.parent(parent)
        if parent.data < grand_parent.data:
            return grand_parent.right.data
        if parent.data > grand_parent.data:
            return grand_parent.left.data

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        self._insertNode(data,self.root)

    def _insertNode(self,data,node):
        if data < node.data:
            if node.left:
                self._insertNode(data,node.left)
            else:
                node.left = Node(data)
        if data > node.data:
            if node.right:
                self._insertNode(data,node.right)
            else:
                node.right = Node(data)
        #return self.violation(node)
