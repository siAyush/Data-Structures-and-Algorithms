'''
The KMP matching algorithm uses degenerating property (pattern having same
sub-patterns appearing more than once in the pattern) of the pattern and
improves the worst case complexity to O(n). The basic idea behind KMP’s
algorithm is: whenever we detect a mismatch (after some matches), we already
know some of the characters in the text of the next window. We take advantage
of this information to avoid matching the characters that we know will anyway match.
'''
def kmp(text,pattern):
    n = len(text)                         # length of text
    m = len(pattern)                      # length of pattern
    if m == 0:
        return None
    fail = kmp_fail(pattern)
    t = 0                                # index into text
    p = 0                                # index into pattern
    while t < n:
        if text[t] == pattern[p]:
            if p == m-1:                 # match is complete
                return t-m+1
            t += 1
            p += 1
        elif p > 0:
            p = fail[p-1]                   # reuse suffix of pattern[0:p]
        else:
            t += 1
    return None

def kmp_fail(pattern):
    '''
    utility that computes and return kmp list
    '''
    m = len(pattern)
    fail = [0]*m
    j = 1
    k = 0
    while j < m:
        if pattern[j] == pattern[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail
a = 'ababababababc'
b = 'abc'
print(kmp(a,b))
