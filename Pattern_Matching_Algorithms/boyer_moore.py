def boyer_moore(text,pattern):
    n = len(text)                         # lenght of text
    m = len(pattern)                      # length of pattern
    if m == 0:
        return None
    last = {}                             # build 'last' dictionary
    for k in range(m):
        last[pattern[k]] = max(1,m-k-1)   # bad match table
    t = m-1                               # an index into text
    p = m-1                               # an index into pattern
    while t < n:
        if text[t] == pattern[p]:
            if p == 0:
                return t
            else:
                t -= 1
                p -= 1
        else:
            if last.get(text[t]):
                t = last.get(text[t]) 
            p = m-1
    return None
a = 'this is a test'
b = 'test'
print(boyer_moore(a,b))
