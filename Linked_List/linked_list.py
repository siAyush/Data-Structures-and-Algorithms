'''
Linked list is a sequence of elements in which every element has link
to its next element in the sequence.Linked list does not support indexing.
'''
class Node():                        # Node Class
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self._size = 0                # number of elements in linked list
        self.head = None             # reference to the head node

    def size(self):
        'return the number of elements in linked list'
        return self._size

    def is_empty(self):
        'return true if linked list is empty'
        if self._size == 0:
            return True
        else:
            return False

    def insert_start(self,e):
        'add element at the start of linkedlist'
        newNode = Node(e)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def remove(self,e):
        'remove any element from the linkedlist'
        if self.size == 0:
            print('linkedlist is empty')
        currentN = self.head             # current Node
        previousN = None                    # previous Node
        while currentN.data != e:
            previousN = currentN
            currentN = currentN.next
        if previousN is None:              # if element is head node
            self.head = currentN.next
        else:
            previousN.next = currentN.next
        self.size -= 1

    def pop(self):
        'remove the first(lastly added) element'
        removed = self.head
        self.head = self.head.next
        self.size -= 1
        return removed

    def insertEnd(self,data):
        'add element at the end of linkedlist'
        currentN = self.head
        newNode = Node(data)
        while currentN.next != None:
            currentN = currentN.next
        currentN.next = newNode
        self.size += 1

    def traverse(self):
        'print all elements of linkedlist'
        currentN = self.head
        while currentN != None:
            print('Node data %d'%currentN.data)
            currentN = currentN.next
