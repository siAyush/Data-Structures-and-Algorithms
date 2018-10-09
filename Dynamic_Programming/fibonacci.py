def fib(n,memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1,memo)+fib(n-2,memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None]*int(n+1)
    return fib(n,memo)
