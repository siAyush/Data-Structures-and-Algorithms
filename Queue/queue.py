'''
This is the implementation of queue in python 3.So, queue works on principle
'First in First Out (FIFO)'.This implementation uses adapter design pattern to
adapt list class of python3.
'''
class Queue():
    def __init__(self):
        self._queue = []           # list work as uqeue

    def __len__(self):
        'return length of queue'
        return len(self._queue)

    def enqueue(self,item):
        'add item to the queue'
        self._queue.append(item)

    def dequeue(self):
        'remove the first item'
        if len(self._queue) == 0:
            print('Queue is empty')
        else:
            self._queue.pop(0)

    def first(self):
        'return the first item of queue'
        if len(self._queue) == 0:
            print('Queue is empty')
        else:
            return self._queue[0]


    def is_empty(self):
        'check queue is empty or not.'
        if len(self._queue) == 0:
            print('Queue is empty')
        else:
            print('Queue is not empty')
