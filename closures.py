"""Closures"""

# A closure is when a fn accesses a variable outside of its scope:

counter = 0
def count():
    # have to tell fn that it's looking for a globally defined variable
    global counter
    # print it
    print counter
    # increment it
    counter += 1

# in the above, the fn has access to counter as a global variable, outside of
# itself. This makes count() a 'closure'.

>>> count()
0
>>> count()
1
>>> count()
2  # but, the 'counter' variable could get messed up somewhere else:
>>> counter = 0
>>> count()
0  #oops!! 

# So, we can wrap it as a private variable in an outside fn:

def counter_outer():
    # we need to wrap it in a list, so it is mutable
    counter = [0]
    # define the inside fn
    def count_inner():
        # increment before returning
        counter[0] += 1
        print counter[0]
    # return a REFERENCE to the inner fn (don't call it here!!)
    return count_inner

"""
>>> def counter_outer():
...     counter = [0]
...     def count_inner():
...             counter[0] += 1
...             print counter[0]
...     return count_inner
... 
>>> counter_1 = counter_outer()
>>> counter_2 = counter_outer()
>>> counter_1()
1
>>> counter_1()
2
>>> counter_1()
3
>>> counter_2()
1
>>> counter_1()
4

"""

# now, counter_outer() has closed over the variable 'counter', so each 
# instantiation of the function counter() (i.e. counter_1 and counter_2) have 
# different 'counter' variables for themselves. This way, we can reuse the 
# same variable in different instances. 

# This is very common practice in javascript - by using inline fn's

# In Python, other clever ways to do this - hide a variable for use by 
# different instances - is with classes or generator objects: 

class Counter:
    def __init__(self):
        self.counter = 0

    def count(self):
        self.counter += 1
        print self.counter

"""
>>> class Counter(object):
...     def __init__(self):
...             self.counter = 0
...     def count(self):
...             self.counter += 1
...             print self.counter
... 
>>> counter_1 = Counter()
>>> counter_2 = Counter()
>>> counter_1.count()
1
>>> counter_1.count()
2
>>> counter_1.count()
3
>>> counter_2.count()
1
"""


