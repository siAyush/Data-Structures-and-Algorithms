'''
A delimiter is a sequence of one or more characters used to specify the boundary
between separate, independent regions in plain text or other data streams.
( )	Parentheses
{ }	Braces (also called curly brackets)
[ ]	Brackets
< >	Angle brackets
" "	commonly used to denote string literals.
' '	commonly used to denote character literals.
'''
def d_match(text):
    left ='({[<''
    right = ')}]>'
    
