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
            # node with two childs
            temp = self._getPredecessor(node.leftchild)
            node.data = temp.data
            node.leftchild = self._removeNode(temp.data,node.leftchild)
        return node

    def _getPredecessor(self,node):
        current = node.rightchild
        while current != None:
            current = current.rightchild
        return node

    def in_order_traverse(self):
        'in order traverse'
        if self.root:
            self._in_order_traverse(self.root)

    def _in_order_traverse(self,node):
        if node.leftchild:
            self._in_order_traverse(node.leftchild)
        print('Node data %s'%node.data)
        if node.rightchild:
            self._in_order_traverse(node.rightchild)

    def pre_ordre_traverse(self):
        'pre order traverse'
        if self.root:
            self._pre_order(self.root)

    def _pre_order(self,node):
        print('Node data %s'%node.data)
        if node.leftchild:
            self._pre_order(node.leftchild)
        if node.rightchild:
            self._pre_order(node.rightchild)

    def post_order_traverse(self):
        'post order traverse'
        if self.root:
            self._post_order(self.root)

    def _post_order(self,node):
        if node.leftchild:
            self._post_order(node.leftchild)
        if node.rightchild:
            self._post_order(node.rightchild)
        print('Node data %s'%node.data)

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

    def height_of_tree(self):
        'Reurn the height of tree'
        if self.root:
            return self._height(self.root)

    def _height(self,node):
        if not node:
            return -1
        left_tree = self._height(node.leftchild)
        right_tree = self._height(node.rightchild)
        height = max(left_tree,right_tree)+1
        return height

    def delete_tree(self):
        'It delete the whole tree.'
        del self.root
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def breadth_first_search(self):
        'Print all elements of tree in breadth first search manner.'
        queue = []
        if self.root:
            queue.append(self.root)                    # store visited nodes
        while len(queue) != 0:
            node = queue[0]
            if node.leftchild:
                queue.append(node.leftchild)
            if node.rightchild:
                queue.append(node.rightchild)
            print(queue.pop(0).data)











bst = Binary_Tree();
bst.insert(10);
bst.insert(13);
bst.insert(5);
bst.insert(14);
bst.post_order_traverse()
#bst.breadth_first_search()
