'''
Brute Force Search enumerate all possible configurations of inputs involved
and picks the best(pattern matched) of all these enumerated configurationsself.

Keep iteration through the text and if there is mismatch we shift the pattern
one step to the right.
'''

def brute_force_search(text,pattern):
    n = len(text)           # length of text
    m = len(pattern)        # length of pattern
    for i in range(n-m+1):
        k = 0               # an index into pattern
        while k < m and text[i+k] == pattern[k]:
            k += 1
        if k == m:
            return i
    return None            # failed to find match 
