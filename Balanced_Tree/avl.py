'''
AVL Tree named after the initials of its inventors Adel'son-Vel'skii and Landis.
AVL tree is just like BST(Binary Search Tree) with one difference that
they are more balanced than BST(Binary Search Tree) and they guaranteed
Big-O(log-N) complexity.
'''

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0

class AVL():
    def __init__(self):
        self.root = None

    def insert(self,data):
        'Insert the data in tree.'
        self.root = self._insertNode(data,self.root)

    def _insertNode(self,data,node):
        if not node:
            return Node(data)
        if data < node.data:
            if node.left_child is not None:
                self._insertNode(data,node.left_child)
            else:
                node.left_child = Node(data)

        if data > node.data:
            if node.right_child is not None:
                self._insertNode(data,node.right_child)
            else:
                node.right_child = Node(data)
        node.height = max(self.calcHeight(node.left_child),self.calcHeight(node.right_child))+1
        return self.violation(data,node)

    def in_order_traverse(self):
        'in order traverse'
        if self.root:
            self._in_order_traverse(self.root)

    def _in_order_traverse(self,node):
        if node.left_child:
            self._in_order_traverse(node.left_child)
        print('Node data %s'%node.data)
        if node.right_child:
            self._in_order_traverse(node.right_child)

    def calcHeight(self,node):
        'return the height of node'
        if node is None:
            return -1
        return node.height

    def calcBalance(self,node):
        """calculate the difference between the heights of left and right subtrees"""
        if node is None:
            return 0
        return self.calcHeight(node.left_child) - self.calcHeight(node.right_child)

    def rotate_left(self,node):
        node_right_child = node.right_child
        node_right_child_left_child = node_right_child.left_child
        node_right_child.left_child = node
        node.right_child = node_right_child_left_child
        node.height = max(self.calcHeight(node.left_child),self.calcHeight(node.right_child))+1
        node_right_child.height = max(self.calcHeight(node_right_child.left_child),self.calcHeight(node_right_child.right_child))+1
        return node_right_child

    def rotate_right(self,node):
        node_left_child = node.left_child
        node_left_child_right_child = node_left_child.right_child
        node_left_child.right_child = node
        node.left_child = node_left_child_right_child
        node.height = max(self.calcHeight(node.left_child),self.calcHeight(node.right_child))+1
        node_left_child.height = max(self.calcHeight(node_left_child.left_child),self.calcHeight(node_left_child.right_child))+1
        return node_left_child


    def violation(self, data, node):
        balance = self.calcBalance(node)
        # left left heavy situation
        if balance > 1 and data < node.left_child.data:
            print("Left left heavy tree...")
            return self.rotate_right(node)
        # right right heavy situation
        if balance < -1 and data > node.right_child.data:
            print("Right right heavy tree...")
            return self.rotate_left(node)
        # left right situation
        if balance > 1 and data > node.left_child.data:
            print("Tree is left right heavy...")
            node.left_child = self.rotate_left(node.left_child);
            return self.rotate_right(node)
        # right left situation
        if balance < -1 and data < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child);
            return self.rotate_left(node)
        return node



avl = AVL()
avl.insert(2)
avl.insert(1)
avl.insert(0)
avl.in_order_traverse()
