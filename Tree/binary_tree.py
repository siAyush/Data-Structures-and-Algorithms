'''
Binary Tree is a non-linear, hierarchical data structuresself.
In Binary tree every node can have at most two child (left child and left child).
'''

# Node
class Node():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

# Tree
class Binary_Tree():
    def __init__(self):
        self.root = None

    def insert(self,data):
        'Insert the data in tree.'
        if not self.root:
            self.root = Node(data)
        else:
            self._insertNode(data,self.root)

    def _insertNode(self,data,node):
        if data < node.data:
            if node.leftchild:
                self._insertNode(data,node.leftchild)
            else:
                node.leftchild = Node(data)
        if data > node.data:
            if node.rightchild:
                self._insertNode(data,node.rightchild)
            else:
                node.rightchild = Node(data)

    def remove(self,data):
        'Remove data from tree.'
        if self.root:
            self.root = self._removeNode(data,self.root)

    def _removeNode(self,data,node):
        if not node:
            return node
        if data < node.data:
            node.leftchild  = self._removeNode(data,node.leftchild)
        elif data > node.data:
            node.rightchild = self._removeNode(data,node.rightchild)
        else:
            if not node.leftchild and not node.rightchild:   # leaf Node
                del node
                return None
            elif not node.leftchild:               # node with no leftchild
                temp = node.rightchild
                del node
                return temp
            elif not node.rightchild:             # node with no rightchild
                temp = node.leftchild
                del node
                return temp
            # node with both childs
            temp = self._getPredecessor(node.leftchild)
            node.data = temp.data
            node.leftchild = self._removeNode(temp.data,node.leftchild)
        return node

    '''def _getPredecessor(self,node):
        if node.rightchild:
            return self._getPredecessor(node.rightchild)
        return node'''
    def _getPredecessor(self,node):
        current = node.rightchild
        while current != None:
            current = current.rightchild
        return node

    def traverse(self):
        'Print all elements of tree (traverse in order).'
        if self.root:
            self._traverse_in_order(self.root)

    def _traverse_in_order(self,node):
        if node.leftchild:
            self._traverse_in_order(node.leftchild)
        print('Node data %s'%node.data)
        if node.rightchild:
            self._traverse_in_order(node.rightchild)

    def getMax(self):
        'Return the max value of tree'
        current  = self.root
        while current.rightchild != None:
            current = current.rightchild
        return current.data

    def getMin(self):
        'Return the min value of the tree'
        current = self.root
        while current.leftchild != None:
            current = current.leftchild
        return current.data



bst = Binary_Tree();
bst.insert(10);
bst.insert(13);
bst.insert(5);
bst.insert(14);
#print(bst.getMin())
bst.remove(10)
#print(bst.root.data)
#print(bst.)
bst.traverse()
