"""Data Structures"""

"""Arrays"""
# ARRAYS (low-level)
# Low level array is an ORDERED collection of elements at INDEX positions. 
# When creating, must specify length. 
# Look up is O(1) because the index stores memory location. 

# STRINGS are almost always a (low-level, IMMUTABLE) array of characters. 

# DYNAMIC ARRAYS (LISTS)
# Higher level, or dynamic arrays (like 'lists' in Python), allows you to 
# insert and delete, or modify length. They are MUTABLE. 

# Runtime analysis of dynamic array: 
# Let's say pushing to a list with no more space doubles it's length. 
# What is the runtime of pushing to a list of length n, m times? 

# 1) Asymptotic Analysis: 
#    Worst case scenario: O(m) time per insertion, O(m) time to double: O(m^2)
# 2) Amortized Analysis:
#    a) Aggregate Analysis: push = 1 + 2 + 4 + 8 + ... + n/2 + n = O(2m) = O(m)
#    b) Banking Method: $2 per push after mid point to pay for copying itself
#       and copying one before mid point when doubling occurs. Plus $1 for the
#       original insert of itself. So $3 per push. That's consatant: O(m)


"""Hash Maps"""
# HASH TABLE (HASH, HASH MAP, MAP, DICTIONARY)
# Pairs keys to values:
    lightbulb_hours_of_light = {
        'incandescent': 1200,
        'compact fluorescent': 10000,
        'LED': 50000
    }

# Runtime for insertion and lookup: O(1)

# Hash tables are UNORDERED (not stored by index or position, only by key)
# Can use any unmutable type as key, so key can be hashed. 
# Built on arrays, using indecies as maps from hashes of keys. 
# Things can get complicated when hashes collide. There are algorithms that 
# make mapping save space and time to handle collisions, like adding an odd
# number to the collision, doubling the length of the array and making a copy, 
# double hashing, using a longer hash, etc. 


"""Linked Lists"""
# LINKED LIST
# Low level data structure storing an ORDERED list of objects as data on 'nodes'
# and pointers to the next node. 
    class LinkedListNode:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    class LinkedList:
        def __init__(self, head=None, tail=None):
            self.head = head
            self.tail = tail

    a = LinkedListNode('a')
    b = LinkedListNode('b')
    c = LinkedListNode('c')

    a.next = b
    b.next = c

    alphabet = LinkedList()
    alphabet.head = a
    alphabet.tail = c

# Linked List vs. Array (both ordered, mutable):
# LL has constant time insertion and deletion. Array takes O(n) at front. 
# Resizing LL is constant, vs. array where doubling occurs. 
# Accessing middle of LL requires walking list, vs. array O(1) lookup by index. 

# DOUBLY LINKED LIST
# add a 'previous' attribute, in addtion to value and next. 


"""Queues"""
# QUEUE
# A queue is like a line at a coffee shop: First in, first out (FIFO). 
# A queue has the trade off of O(n) runtime for EITHER insertion or removal. 
# This could be fixed with a linked list, but that trades time for space. 

class Queue:
    # initialize as an empty list
    def __init__(self):
        self.queue = []

    # add items to the end of the list (constant runtime)
    def enqueue(self, item):
        self.queue.append(item)

    # pop items from the front of the list (this is O(n) b/c of re-indexing)
    def dequeue(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return not self.queue


"""Stacks"""
# STACK
# A stack is like pancakes: last in, first out (LIFO)
# A stack is constant runtime for adding or removing items. 

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack



"""Trees"""
# TREE 
# An organizational hirearchy of nodes with data and more nodes as children. 

class TreeNode:
    # this is naive, as the children list will be the SAME list in memory
    # for all nodes created. A better way, below. 
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    # better way:
    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), "children must be a list!"
        self.data = data
        self.children = children

    def find_node(self, data):
        """Return node with matching data"""

        # use a stack for depth first search, a queue for breadth first search
        to_visit = [self]

        while to_visit:
            # using a stack, take the first item from top (starting with self)
            node = to_visit.pop(0)
            if node.data == data:
                return node
            # if the data doesn't match, add children to to_visit and continue
            to_visit.extend(node.children)

        # if all nodes are exhausted (to_visit is empty)
        return "Node not found"


class Tree:
    def __init__(self, root=None):
        self.root = root

    def find_node_in_tree(self, data):
        """Return a node with matching data"""
        # use the find_node method on root of tree
        return self.root.find_node(data)


# BIANARY TREES
# In a bianary tree, every node has two or fewer children.
# In a bianary search tree, all left nodes are less than, all right are greater.
# Interesting properties:
# 1) number of nodes on each level doubles (if 'perfect'/no-gap tree)
# 2) number nodes bottome level = half the num of all other nodes + 1
#    level 0: 1 node = 2^0
#    level 1: 2 nodes = 2^1
#    level 2: 4 nodes = 2^2, etc.
#    total nodes, n = 2^0 + 2^1 + 2^2 + ... + 2^(h-1), where h is height
#    or, n = 2*(num nodes on bottom level) -1
#    we know (num nodes on bottom level) = 2^(h-1), so:
#    n = 2 * [2^(h-1)] - 1
#    n = 2^1 * 2^(h-1) - 1
#    n = 2^(1 + h - 1) - 1
#    n = 2^h -1
#    n + 1 = 2^h
#    lg(n+1) = lg(2^h) = h * lg(2) = h * 1
#    lg(n+1) = h

# in summary: 
#   the total numbe of nodes, n, in a perfect bianary tree:
#       n = 2^h - 1
#   the height of a tree, h, relative to the number of nodes:
#       h = lg(n+1)


class BianaryNode:
    def __init__(self, data, left=None, right=None):
        assert left is None or isinstance(left, BinaryNode)
        assert right is None or isinstance(right, BianaryNode)
        self.data = data
        self.left = left
        self.right = right


"""Graphs"""
# GRAPH
# A graph is a cyclic tree - they can be directional, 
# but they're not hierarchical. Each node has data and adjacent nodes. 
# Adjacencies can overlap. 

class GraphNode:
    """Stores data and adjacent connections"""
    def __init__(self, data, adjacent=None):
        assert adjacent = None or isinstance(adjacent, set), \
            "adjacencies must be a set!"
        self.data = data
        self.adjacent = adjacent

    def add_adjacencies(self, adjacencies):
        """Add adjacencies to the node"""
        assert isinstance(adjacencies, set()), "adjacencies must be a set!"
        self.adjacenct.add(adjacencies)


class Graph:
    """Stores a set of nodes"""
    def __init__(self):
        self.nodes = set()

    def add_node(self, data):
        """Create node from data, add to graph set"""
        self.nodes.add(GraphNode(data))

    def find_connection_iteratively(self, data1, data2):
        """Use breadth first search to see if two nodes are connected"""

        # make a queue of nodes to look for data2
        possible_nodes = Queue()
        possible_nodes.enqueue(data1)

        # make a set of nodes that have been checked already
        seen = set()

        # while there are still nodes to visit:
        while not possible_nodes.is_empty():
            # take the first node out of the queue to check
            current = possible_nodes.dequeue()
            # if the node matches the sought, return True
            if current == data2:
                return True
            # otherwise, add the current to the seen set
            seen.add(current)
            # find the unseen adjacencies of the current
            unseen_adjacencies = current.adjacent - seen
            # add each unseen node to the que and continue checking
            for unseen in unseen_adjacencies:
                possible_nodes.enqueue(unseen)


    def find_connection_recursively(self, data1, data2, seen=None):
        """Use recursion (depth-first search with callstack) to find connect"""

        # base case: found connection
        if data1 == data2:
            return True

        # base case: seen set is empty, so make a new one
        if not seen:
            seen = set()

        # progress toward base case: 
        # add current to seen set
        seen.add(data1)
        # get unseen adjacencies, check each for connection:
        unseen_adjacencies = data1.adjacenct - seen
        for unseen in unseen_adjacencies:
            if find_connection_recursively(unseen, data2, seen):
                # if returned out of callstack, unseen == data2
                return True

        return False


"""Summary of Data Structures"""
# RUNTIMES
# Array/list:
# Index:    constant
# Search:   linear
# Add-R:    constant
# Add-L:    linear
# Pop-R:    constant
# Pop-L:    linear

# Singly Linked List:
# Index:    linear
# Search:   linear
# Add-R:    constant
# Add-L:    constant (w/ head)
# Pop-R:    linear
# Pop-L:    constant (w/ head)

# Doubly Linked List:
# Index:    linear
# Search:   linear
# Add-R:    constant
# Add-L:    constant
# Pop-R:    constant
# Pop-L:    constant

# Queue (as array):
# Index:    -
# Search:   -
# Add-R:    constant
# Add-L:    -
# Pop-R:    -
# Pop-L:    linear

# Queue (as LL/DLL):
# Index:    -
# Search:   -
# Add-R:    constant
# Add-L:    -
# Pop-R:    -
# Pop-L:    constant

# Stack (as array/LL/DLL):
# Index:    -
# Search:   -
# Add-R:    constant
# Add-L:    -
# Pop-R:    constant
# Pop-L:    -

# Deque (as DLL):
# Index:    -
# Search:   -
# Add-R:    constant
# Add-L:    constant
# Pop-R:    constant
# Pop-L:    constant


# MEMORY/SPACE COMPLEXITY
# Hash Map
# Get:      constant
# Add:      constant
# Delete:   constant
# Iterate:  linear
# Memory:   medium

# Set (like hash map of just keys):
# Get:      constant
# Add:      constant
# Delete:   constant
# Iterate:  linear
# Memory:   medium

# Bianary Search Tree:
# Get:      lg(n)
# Add:      linear (b/c could req re-balance)
# Delete:   linear (b/c could req re-balance. Del leaf is constant)
# Iterate:  constant (just one node to next, b/c of pointer)
# Memory:   small (why?)

# Tree:
# Get:      linear
# Add:      constant (if you know where it goes)
# Delete:   constant (if you know where it is)
# Iterate:  constant (just from one to the next, b/c of pointer)
# Memory:   small

# Ordered Set (Hash map + DLL):
# Get:      constant
# Add:      constant
# Delete:   constant
# Iterate:  constant
# Memory:   huge

# Ordered Dict (Hash map + DLL):
# Get:      constant
# Add:      constant
# Delete:   constant
# Iterate:  constant
# Memory:   huge
