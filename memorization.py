"""Memorization"""

# Sometimes a problem repeats the same work multiple times, wasting time/space. 
# Example: recursive fibnacci:

def fibonacci_recursive(n):
    """returns the n'th fibonacci number. Starts: 0, 1, 1, 2, 3, 5, 8,..."""

    # The first two numbers must be given, since there are not enough previous
    if n in [0, 1]:
        return n

    # else, return the sum of the previous two
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# To avoid recalling things like fibonacci_recursive(2) a bunch of times, 
# use memorization. 

# To memorize, wrap the fn in a class that stores outputs of common calls:

def fibonacci_iteratively(n):
    """Returns the n'th fibonacci number"""

    # edge case:
    if n < 0:
        raise Exception("Can't have a negative fibonacci index!")

    # base case: first two numbers must be given, not enough previous
    if n in [0, 1]:
        return n

    # initialize the two previous numbers, starting with n=2
    prev1 = 1
    prev2 = 0

    # iterate over range given, adding previous two and re-assigning variables
    for i in range(n):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return current

# use a class wrapper to use a dictionary to memorize common problems
class Fibber:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        """Returns n'th fib number, uses recursion & memorization"""

        # edge case:
        if n < 0:
            raise Exception("Can't have a negative fibonacci index!")

        # base case: first two numbers must be given, not enough previous
        if n in [0, 1]:
            return n

        # see if solution has been memorized
        if n in self.memo:
            reutrn self.memo[n]

        # else, recurse, saving results to memo
        result = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = result

        return result

# This works. Another solution to dynamic programming (solution composed of 
# overlapping subproblems of the same problem). Another one is "bottom up". 
# See notes for bottom up... 









