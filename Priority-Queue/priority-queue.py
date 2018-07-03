'''
A priority queue is an abstract data type
which is like a regular queue or stack data structure, but where
additionally each element has a "priority" associated with it.
In a priority queue, an element with high priority is served before
an element with low priority. If two elements have the same
priority, they are served according to their order in the queue.

While priority queues are often implemented with heaps, they are
conceptually distinct from heaps. A priority queue is an abstract
concept like "a list"  just as a list can be implemented
with a linked list or an array, a priority queue can be implemented
with a heap.
# NOTE: This is a minimum oriented Priority Queue implementation with binary heap.
'''

class Item():
    # key = priority of that value
    # value = data
    def __init__(self,key,value):
        self.key = key
        self.value = value

class PriorityQueue():

    def __init__(self):
        self.data = []

# --------------------------nonpublic behaviors--------------------------------

    def _parent(self,j):
        return (j-1)//2

    def _left_child(self,j):
        return 2*j+1

    def _right_child(self,j):
        return 2*j+2

    def _has_left(self,j):
        return self._left_child(j) < len(self.data)

    def _has_right(self,j):
        return self._right_child(j) < len(self.data)

    def _swap(self,i,j):
        'swap the elements at indices i and j of array.'
        self.data[i],self.data[j] = self.data[j],self.data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self.data[j].key < self.data[parent].key:
            self._swap(j,parent)
            self._upheap(parent)

    def _downheap(self,j):
        if self._has_left(j):
            left = self._left_child(j)
            child_to_swap = left
            if self._right_child(j):
                right = self._right_child(j)
                if self.data[right].key < self.data[left].key:
                    child_to_swap = right
                if self.data[child_to_swap].key < self.data[j].key:
                    self._swap(j,child_to_swap)
                    self._downheap(child_to_swap)

# -----------------------------public behaviors---------------------------------

    def __len__(self):
        'Return the number of items in the Priority Queue.'
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def add(self,key,value):
        'Add key-value pair to the Priority Queue.'
        self.data.append(Item(key,value))
        self._upheap(len(self.data)-1)

    def min(self):
        'Return but do not remove (key,value)tuple with minimum key.'
        if self.is_empty():
            return None
        return ('Key = %d , Value = %d'%(self.data[0].key,self.data[0].value))

    def remove_min(self):
        'Remove and return (key,value) tuple with minimum key.'
        if self.is_empty():
            return None
        self._swap(0,len(self.data)-1)
        item = self.data.pop()
        self._downheap(0)
        return ('Key = %d , Value = %d'%(item.key,item.value))
