''' Memoization for Fibonacci sequence calculation'''

def fib(n):
    memo={}
    return _fib(n,memo)

def _fib(n,memo):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in memo:
        return memo[n]


    memo[n] = _fib(n-1,memo) + _fib(n-2,memo)
    return memo[n]


print(fib(7))    