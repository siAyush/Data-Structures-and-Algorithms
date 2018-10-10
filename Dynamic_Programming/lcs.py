"""
Longest Common Subsequence (lcs) using dynamic programming.
"""

data = [[None]*m+1 for i in range(n+1)]


def lcs(p, q, n, m):
    if data[n][m] is not None:
        return data[n][m]

    if n == 0 or m == 0:
        result = 0

    elif p[n-1] == q[m-1]:
        result = 1+lcs(p, q, n-1, m-1)

    elif p[n-1] != q[m-1]:
        temp1 = lcs(p, q, n-1, m)
        temp2 = lcs(p, q, n, m-1)
        result = max(temp1, temp2)
    data[n][m] = result
    return result