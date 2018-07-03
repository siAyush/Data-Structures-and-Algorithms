'''
Heap is generally preferred for priority queue implementation because heap
provide better performance compare to array(list).
This implementation is for maximum heap.
'''
class Heap():
    def __init__(self):
        self.heap = []

    def insert(self,data):
        'Add the new item in Heap.'
        self.heap.append(data)
        position = self.heap.index(self.heap[-1])
        self.fixup(position)


    def fixup(self,index):
        parent_index = (index-1)//2
        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]
            index = parent_index
            parent_index = (index-1)//2

    def heapsort(self):
        'Print elements of in decreasing order.'
        for i in range(len(self.heap)):
            print(self.heap[0])
            #print(self.heap)
            self.heap[0],self.heap[len(self.heap)-i-1] = self.heap[len(self.heap)-i-1],self.heap[0]
            upto = len(self.heap)-i-2
            self.fixdown(0,upto)

    def fixdown(self,index,upto):
        while index <= upto:
            leftchild = 2*index+1
            rightchild = 2*index+2
            if leftchild < upto:
                child_to_swap = None
                if rightchild > upto:
                    child_to_swap = leftchild
                else:
                    if self.heap[leftchild] < self.heap[rightchild]:
                        child_to_swap = rightchild
                    else:
                        child_to_swap = leftchild
                if self.heap[index] < self.heap[child_to_swap]:
                    self.heap[index],self.heap[child_to_swap] = self.heap[child_to_swap],self.heap[index]
                else:
                    break
                index = child_to_swap
            else:
                break
