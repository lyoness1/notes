"""Bianary Search"""

# Bianary search finds an item in a SORTED arry in O(lg(n)) time. 

# Step 1) Start in middle - is target higher or lower? 
# Step 2) Problem divided in half. Go left or right. 
# Step 3) Pick a new middle. Repeat. 

# Can be recursive, or iterative. 


# EXAMPLE: Using Bianary Search Tree

class BianaryNode:
    def __init__(self, data, left=None, right=None):
        assert left is None or isinstance(left, BianaryNode), "left must be a node"
        assert right is None or isinstance(right, BianaryNode), "right must be a node"
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        assert isinstance(root, BianaryNode), "root must be a node"
        self.root = root

    def bianary_search_iterative(self, node):
        """Returns matching node"""

        # make sure the tree has at least one node
        if not self.root:
            return "Tree is empty"

        current_node = self.root

        while current_node:
            if current_node.data == node.data:
                return current_node
            elif current_node.data < node.data:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return "Node does not exist in tree"


    def bianary_search_recursive(self, node):
        """Returns matching node"""

        def _recurser(self, target_node, current_node):
            """Helper function to use as recurser"""

            # base case: found node
            if current_node == target_node:
                return current_node

            # if not found, recurse progressively
            if target_node.data < current_node.data:
                _recurser(target_node, current_node.left)
            _recurser(target_node, current_node.right)

        # make sure tree isn't empty:
        if not self.root:
            return "Tree is empty"

        _recurser(node, self.root)


# EXAMPLE: Bianary search in a sorted array

def bianary_search_iterative(target, arr):
    """Returns True if target is found in sorted arr"""

    low_index = 0
    high_index = len(arr)

    while high_index > low_index:
        guess_index = (high_index - low_index) / 2
        guess = arr[guess_index]
        if guess == target:
            return True
        elif guess < target:
            low_index = guess_index
        high_index = guess_index

    return "target is not in arr"








