"""Big O Notation"""

# Big-O is notation for RUNTIME of a problem. 
# Bio-O compares EFFICIENCY of different solutions. 
# Bio-O measures how quickly a problem grows RELATIVE TO THE LENGTH OF THE INPUT

# 1. How quickly runtime grows:
#    Hard to compare exact runtimes, b/c depends on machine. 
#    Instead, Bio-O compares how quickly runtime GROWS, relative to input. 

# 2. Relative to input: 
#    Need something to base growth from. Use input (generally, n)

# 3. As input grows, or gets arbitrarily long: 
#    Some steps may seem expensive with small n, but will pay off with large n.


# Examples: 
# O(1): only one step, regardless of size of lst
def print_first(lst):
    print lst[0]

# O(n): always as many steps as length of lst
def print_all(lst):
    for item in lst:
        print item

# O(n^2): must always iterate over list twice (with this solution):
def print_pairs(lst):
    for idx in range(len(lst)):
        for item in lst:
            print lst[idx], item

# NOTE: n can be the length of the input, or the size of the input. A list of 
# length n and a range of length n are the same size, but one is a list and one
# is an integer. 

# CONSTANTS & LESS SIGNIFICANT TERMS
# Big-O throws out the constants. 
# So, n + n = 2n becomes runtime n, still. 
# Or, 1 + n + 100 = 101 + n is runtime n, still. For big n, 101 is negligible. 
# Finally, n^2 + n is runtime O(n^2), because that is fasteset growing term. 

# ASSUME WORST CASE
# Sometimes, you find the needle in the haystack on your first try. Sometimes, 
# it takes an average number of tries. Sometimes, it's the last try. Bio-O 
# always assumes it's the last try, or the worst case scenario. 


# SPACE COMPLEXITY
# Sometimes size is more important (or, also important) than time. 
# Space complexity measures how much ADDITIONAL space is used, compared to input


# Examples:
# O(1) space: no additional (to the integer n) space used
def print_n_things(n):
    for i in range(n):
        print i

# O(n): create a list of size n, in addition to the integer n provided
def print_n_things(n):
    n_things = []
    for i in range(n):
        n_things.append(i)
    print n_things


# NOTE: Beware when constants matter! 
# If runtime is 5 hours, but there's a constant of 4 hours, getting rid of that
# may make Big-O worse, but it's still four hours shorter. Which is better?

# NOTE: Beware premature optimization!
# Sometimes optomizing runtime messes with readability of code, or speed of 
# delivery, which may matter more in some situations. Find the right balance.  
