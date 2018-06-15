'''
Double linked list is a sequence of elements in which every element has links
to its previous element and next element in the sequence.
'''

class Node():                          # Node class
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL():                          # Double linked list (DLL)
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        'return number of elements'
        return self._size

    def is_empty(self):
        'return true if linked list is empty'
        if self._size == 0:
            return True
        else:
            return False

    def insert_start(self,data):
        'add element at the start of doubly linkedlist'
        if self.head is None:
            newNode = Node(data)
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
        self._size += 1

    def insert_end(self,data):
        'add element at the end of doubly linkedlist'
        newNode = Node(data)
        if self.tail is None:
            newNode = Node(data)
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data)
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        self._size += 1

    def insert_after(self,data,after):
        'add element after a given element'
        current = self.head
        while current.next is not None:
            if current.data == after:
                break
            current = current.next
        if current.data == after:
            if current.data == self.tail.data:
                self.insert_end(data)
            else:
                newNode = Node(data)
                old_next = current.next
                current.next = newNode
                old_next.prev = newNode
                newNode.prev = current
                newNode.next = old_next
            self._size += 1
        else:
            print('There is no element %d'%after)

    def insert_before(self,data,before):
        'add element before a given element'
        current = self.head
        while current.next is not None:
            if current.data == before:
                break
            current = current.next
        if current.data == before:
            if current.data == self.head.data:
                self.insert_start(data)
            else:
                newNode = Node(data)
                old_prev = current.prev
                current.prev = newNode
                newNode.next = current
                newNode.prev = old_prev
                old_prev.next = newNode
            self._size += 1
        else:
            print('There is no element %d'%before)

    def insert_in_between(self,data,after,before):
        'add element in between the given elements'
        current = self.head
        while current.next is not None:
            if current.data == after and current.next.data == before:
                break
            current = current.next
        if current.data == after and current.next.data == before:
            newNode = Node(data)
            old_next = current.next
            current.next = newNode
            old_next.prev = newNode
            newNode.prev = current
            newNode.next = old_next
            self._size += 1
        else:
            print('There is no adjacent elements of value %d,%d'%(after,before))

    def traverse(self):
        'print all elements of doubly linkedlist'
        current = self.head
        while current != None:
            print('Node data %d'%current.data)
            current = current.next

    def remove_start(self):
        'it removes the first(last added) element of doubly linkedlist'
        current = self.head.next
        self.head.next.prev = None
        self.head.next = None
        self.head = current
        self._size -= 1

    def remove_end(self):
        'it removes the last element of doubly linkedlist'
        current = self.tail.prev
        self.tail.prev.next = None
        self.tail.prev = None
        self.tail = current
        self._size -= 1

    # TODO:  remove in between
    def remove_in_between(self,data):
        'it removes the given element from doubly linkedlist'
        current = self.head
        while current.next is not None:
            if current.data == data:
                break
            current = current.next
        if current.data == data:
            if current.data == self.head.data:
                self.remove_start()
            elif current.data == self.tail.data:
                self.remove_end()
            else:
                current_prev = current.prev
                current_next = current.next
                current.prev.next = current_next
                current.next.prev = current_prev
                self._size -= 1
        else:
            print('No element of value %d to remove'%data)
