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
        self.size = 0                # number of elements in linked list
        self.head = None             # reference to the head node

    def length(self):
        'return the number of elements in linked list'
        return self.size

    def is_empty(self):
        'return true if linked list is empty'
        if len(self.size) == 0:
            return True
        else:
            return False

    def push(self,e):
        'add element to the linkedlist'
        newNode = Node(e)
        newNode.next = self.head
        self.head = newNode
        self.size += 1



l = LinkedList()
l.push(5)
d = l.length()
print(l.head.data)
print(d)
