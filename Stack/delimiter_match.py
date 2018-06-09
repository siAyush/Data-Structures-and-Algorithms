'''
A delimiter is a sequence of one or more characters used to specify the boundary
between separate, independent regions in plain text or other data streams.
( )	Parentheses
{ }	Braces (also called curly brackets)
[ ]	Brackets
< >	Angle brackets
This function return Yes if expression has both opening and closing delimiter
else it return No.
'''
import re
s = input()
reg = re.compile(r'[\(\)\[\]\{\}]').findall(s)
ri = '([{'
le = ')]}'
# list is used as stack
l = []
k = []
for i in reg:
    if i in ri:
        l.append(i)
    if i in le:
        k.append(i)
if len(k) != len(l):
    print('No')
if len(k) == len(l):
    print('Yes')
