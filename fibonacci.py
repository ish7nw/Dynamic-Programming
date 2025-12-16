def fib(n):
    '''
    A simple method used for computing fibonacci numbers, very time inefficient linear time.
    '''
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_memo(n, memo = None):
    '''
    The same method but the algorithm is designed using the principles of dynamic programming
    Making our algorithm run in polynomial time.
    '''
    if memo is None :
        memo = {}

    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


#print(fib(50))
print(fib_memo(50))