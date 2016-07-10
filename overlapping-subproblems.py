"""Overlapping Subproblems"""

# An Overlapping Subproblem is one where the solution involves solving the same
# problem multiple times. 
# Ex: fibonacci: add previous two, over and over. 

def fibonacci_recursive(n):
    """returns the n'th fibonacci number. Starts: 0, 1, 1, 2, 3, 5, 8,...
    
    >>> fibonacci_recursive(6):
    5

    """

    # The first two numbers must be given, since there are not enough previous
    if n in [0, 1]:
        return n

    # else, return the sum of the previous two
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# This works, but it will repeat some calls multiple times, which is a waste. 
# To fix this, we can use memorization (see other notes)