'''
Double Ended Queue or deque is the extended version of Queue
because in deque you can add and remove form both first and last position
of the Queue.
'''

def Deque():
    def __init__(self):
        self._deque = []

    def add_first(self,e):
        'Add the item in first position.'
        self._deque.insert(0,e)

    def add_last(self,e):
        'Add the item in last position.'
        self._deque.append(e)

    def delete_first(self):
        'Remove item from the first position.'
        self._deque.pop(0)

    def delete_last(self):
        'Remove item from the last position.'
        self._deque.pop()

    def first(self):
        'Return the first item'
        return self._deque[0]

    def last(self):
        'Return the last item'
        return self._deque[-1]

    def __len__(self):
        'Return the length of deque'
        return len(self._deque)

    def is_empty(self):
        'Check deque is empty or not'
        if len(self._deque) == 0:
            print('Deque is empty')
        else:
            print('Deque is not empty')
