'''
A delimiter is a sequence of one or more characters used to specify the boundary
between separate, independent regions in plain text or other data streams.
( )	Parentheses
{ }	Braces (also called curly brackets)
[ ]	Brackets
< >	Angle brackets
'''

from stack import Stack
def d_match(text):
    stk = Stack()
    left ='({[<'
    right = ')}]>'
    for i in text:
        if i in left:
            stk.push(i)
        elif i in right:
            if len(stk) == 0:
                return False
            elif right.index(i) == left.index(stk.pop()):
                print(i + ' delimiter is matched')       # it returns nothing
                                                         # when delimiter is not matched
