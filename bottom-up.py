"""Bottom up solutions to Dynamic Programming problems"""

# solving problems bottom up avoids recursion, saving memory cost of the 
# call stack build up. 

# RECURSION: starts at the top, works backwards by recalling until base case. 
# TOP DOWN: starts at answer, works down to base case.

# ITERATION: loops continuously until solution is found. 
# BOTTOM UP: starts at bottom, works up to answer.

# MEMORIZATION: uses space, saves time, memorizes previous smaller solutions


# EXAMPLE: Factorial

# this recursive, top down solution is runtime O(n) and space O(n) from stack
def factorial_recursively_top_down(n):
    """Returns n!, the product of: n * (n-1) * (n-2) * ... * 1

    >>> factorial_recursively_top_down(5):
    120

    """

    # base case: reach bottom at value 1:
    if n == 1:
        return 1

    # progress down toward base:
    return n * factorial_recursively_top_down(n-1)


# this solution is runtime O(n) and space O(1)
def factorial_iteratively_bottom_up(n):
    """Returns n!, the product of: 1 * 2 * ... * (n-1) * n

    >>> factorial_recursively_bottom_up(5):
    120

    """

    # instantiate a starting value (use 1 for multiplication)
    result = 1

    # iterate over all the numbers up to n, continuously multiplying to result
    for num in range(n):
        result *= num

    return result