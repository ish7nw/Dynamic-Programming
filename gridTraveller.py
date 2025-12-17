def gridTraveller(m, n, memo=None):
    '''
    This method takes in the number of rows and columns in a matrix and returns in how many possible
    ways we can reach from the start to end only using two ways, 
    moving to the right
    moving downwards
    any combination of these two
    '''
    if memo is None:
        memo = {}

    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    key = (m, n)
    if key in memo:
        return memo[key]

    sym = (n, m)
    if sym in memo:
        return memo[sym]

    memo[key] = gridTraveller(m-1, n, memo) + gridTraveller(m, n-1, memo)
    return memo[key]


print(gridTraveller(9, 9))  