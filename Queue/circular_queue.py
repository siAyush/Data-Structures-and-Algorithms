'''
Circular Queue is a linear data structure in which the operations are
performed based on FIFO (First In First Out) principle and the last position
is connected back to the first position to make a circle.
'''

class Circular_Queue():
    default_capacity = 20
    def __init__(self):
        self._cq = [0]*Circular_Queue.default_capacity
        self._front = 0
        self._size = 0

    def __len__(self):
        'Return length of circular queue'
        return self._size

    def is_empty(self):
        'Check queue is empty or not'
        if self._size == 0:
            print('Circular Queue is Empty')
        else:
            print('Circular Queue is Empty')

    def first(self):
        'Return the first item of the Circular Queue'
        if self._size == 0:
            print('Circular Queue is empty')
        else:
            print(self._cq[self._front])

    def dequeue(self):
        'remove and return the first item of Circular Queue'
        if self._size == 0:
            print('Circular Queue is empty')
        item = self._cq[self._front]
        self._cq[self._front] = None
        self._front = (self._front+1)%len(self._cq)
        self._size -= 1
        print(item)

    def enqueue(self,e):
        'add item to the back of queue'
        if self._size == Circular_Queue.default_capacity:
            print('Circular Queue is full')
        else:
            index = (self._front+self._size)%len(self._cq)
            self._cq[index] = e
            self._size += 1
