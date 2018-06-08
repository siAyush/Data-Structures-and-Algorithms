'''
This is the implementation of stack using python3.So, stack works on principle
'First in Last Out (FILO)'.This implementation uses adapter design pattern to
adapt list class of python3.
'''

class Stack():
    def __init__(self):
        self._stack = []         # empty list to store items

    def __len__(self):
        '''return length of stack'''
        return(len(self._stack))

    def push(self,item):
        '''to add items in stack'''
        self._stack.append(item)

    def pop(self):
        '''to remove the last item from stack'''
        if len(self._stack) == 0:
            print('Stack is Empty')
        else:
            return self._stack.pop()

    def top(self):
        '''it's only return the last inserted or top item of the stack'''
        if len(self._stack) == 0:
            print('Stack is Empty')
        else:
            return self._stack[-1]
