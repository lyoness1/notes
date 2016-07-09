"""Logarithms"""

# Logarithms are mainly used to solve for x when x is an EXPONENT. 
# Taking the log of both sides brings the exponent down: 

#        10^x = 100
#   log(10^x) = log(100)
#   x(log 10) = log 100
#           x = 2

# RULES:
# Simplification: logb(b^x) = x(logb(b)) = x
# Multiplication: logb(x*y) = logb(x) + logb(y)
# Division:       logb(x/y) = logb(x) - logb(y)
# Powers:         logb(x^y) = y * logb(x)
# Change of base: logb(x) = logc(x) / logc(b)

# How are Logarithms useful in CS? 
# How many times must I double x to get to n?
# How many times must I cut n in half to get to 1?
# --> Log2(n) for both questions! 


# EXAMPLE: BIANARY SEARCH: algorithm for finding a target num in a SORTED array. 
# 1. Start with middle number - is it bigger or smaller than target? 
# 2. Work has been HALVED!
# 3. Repeat with new middle of half that is left to search. Will continue until
# a) find target, or b) target not in original array. 

# Example: bianary search
def bianary_search(target, arr):
    """Find target in sorted arr of numbers"""

    low_index = 0
    high_index = len(arr)

    # while we are looking at atleast one number
    while low_index < high_index:
        # determind the guess index as halfway between low and high indecies
        middle_index = (high_index - low_index) / 2
        guess_index = low_index + middle_index
        # get the guess value from the guess index
        guess = arr[guess_index]

        # compare guess to target. It will be same, high, or low: 
        if guess == target:
            return True

        elif guess > target:
            high_index = guess_index

        else:
            low_index = guess_index

    # target isn't in arr:
    return False

# What is runtime of bianary search? Worst case scenario, we return False. 
# How many divisions does that take? If len(arr) = n: 
#   n*(1/2)*(1/2)*... = 1   <-- How many 1/2's are there? Let's say: x
#           n*(1/2)^x = 1
#                   n = 2^x
#             log2(n) = log2(2^x)
#             log2(n) = x   <-- We had to divide n in half log2(n) times! 

# Bianary search: O(log(n))


# EXAMPLE: SORTING: Generally (worst case), sorting is O(n * log(n)) 
# This is for COMPARISON BASED sorting. In counting sorting, it's O(n)
# Merge sort is a good example of comparison sorting. 
# Merge sort: 1) divide, 2) sort, 3) compare and combine. 
# Step 2 - sort - can be a recursive call to merge sort again until len(n) = 1

# Example: merge sort
def merge_sort(arr):
    """Sort arr by dividing, sorting, and merging"""

    # base case: length of arr is one
    if len(arr) < 2:
        return arr

    # Step 1: divide arr in half
    left_half = arr[:len(arr)/2]
    right_half = arr[len(arr)/2:]

    # Step 2: sort by recursing on smaller pieces of arr until arr is 1 value
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Step 3: compare and combine
    sorted_output = []

    # if both halves empty, return to call stack or return output, otherwise:
    while sorted_left or sorted_right:
        # if right half is empty, add left's value to output, OR
        # if left is less than right, add left
        if (sorted_left and not sorted_right) or \
                                        (sorted_left[0] < sorted_right[0]):
            sorted_output.append(sorted_left.pop(0))
        # otherwise, add the right
        else:
            sorted_output.append(sorted_right.pop(0))

    return sorted_output

# Runtime is O(n*log(n))
# The O(n) comes from the merging pieces together part
# The O(log(n)) comes from dividing down to arr's 1 value long


# EXAMPLE: BIANARY TREES: Each node has two or fewer children
# In a perfect tree (no gaps, all nodes have 2 children), what is the depth?
# If there are n nodes, let's call the depth h. 
# For 1 node,   n = 1,  h = 1 (1 node, level 1)
# For 3 nodes,  n = 3,  h = 2 (1 node, level 1, 2 nodes, level 2)
# For 7 nodes,  n = 7,  h = 3 (1 level 1, 2 level 2, 4 level 3)
# For 15 nodes, n = 15, h = 4 (1, 2, 4, 8)
# For 31 nodes, n = 31, h = 5 (1, 2, 4, 8, 16, etc.)
# ...The number of nodes on each level DOUBLES
# We double 1 until we get to the number of nodes at the bottom level. 
# The number of nodes at the bottome level is about half n (except, add 1):
# --> HOW MANY TIMES MUST WE DOUBLE 1 TO GET TO: (n+1) / 2
# Height, h, is the number of times we have to double 1 to get to (n+1)/2:

#   h = log2[(n+1)/2] + 1  (adding 1 comes from looking at level 2 example)
#   h = log2(n+1) - log2(2) + 1
#   h = log2(n+1)

# NOTE: Generally, log(x) means log10(x). In CS, log(n) generally means log2(n).
# This is often written lg(n), like ln(x) = loge(x). 




