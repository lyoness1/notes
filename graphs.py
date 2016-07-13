"""Graphs"""

# GRAPH: Network of nodes
# EDGE: Connection between nodes of Graphs
# ARC: Directed edge
# WEIGHTED GRAPH: edges have weights, or distances, or probabilities 

# Desired accomplishments: 
# - find path between nodes
# - find shortest path 
# - find cycle (non-empty path back to original node)
# - find path that hits all nodes (travelling salesman, or 'TSP')

# Making a graph:

# 1) AdjacencyMatrix
#    Four vertecies: A, B, C, D
#    Paths: A --> B, A --> C, B --> C, C --> D, C --> A

nodes = ['A', 'B', 'C', 'D']

# make a matrix of nested lists. 
# Rows are indecies of outer list, col's are indecies of inner lists
AdjacencyMatrix = [ [0] * len(nodes) ] * len(nodes)

paths = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['D', 'A'],
    'D': []
}

# If a path exists, insert a 1 instead of a 0 in the AdjacencyMatrix
# Rows are the starting node, col's are the destination node
# If the edges have weights, insert the weight, rather than just a 1
AdjacencyMatrix = [[0, 1, 1, 0],
                   [0, 0, 1, 0],
                   [1, 0, 0, 1],
                   [0, 0, 0, 0]]


# 2) AdjacencyList
#    for each start node, make a list of destinations
AdjacencyList = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['D', 'A'],
    'D': []
}


# Some examples of algorithms, using sample graph, below
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
         }

# Find a path between two nodes
def find_path(graph, current, destination, path=[]):
    """Returns a path traversed as a list of nodes
        
        >>> find_path(graph, 'A', 'D')
        ['A', 'B', 'C', 'D']

    """

    # add the current node to the path (make a new list)
    path = path + [current]

    # base case: if at destination, return path
    if current == destination: 
        return path

    # account of finding a dead end (current node won't be in destination list)
    if current not in graph: 
        return None

    # recursively keep track of available paths forward
    for node in graph[current]:
        if node not in path: 
            newpath = find_path(graph, node, destination, path)
            if newpath: 
                return newpath
    return None


def find_all_paths(graph, current, destination, path=[]):
    """Returns a path traversed as a list of nodes
        
        >>> find_all_paths(graph, 'A', 'D')
        [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]

    """

    path = path + [current]

    if current == destination:
        return path

    # difference: instead of returning none, return an empty path
    if current not in graph:
        reutrn []

    # create a list for storing the results (because there will be > 1)
    paths = []

    for node in graph[current]:
        if node not in path:
            # the change is to return a list of path lists, instead of one path
            newpaths = find_all_paths(graph, node, destination, path)
            # now, for each path returned, add it to the solutions list
            for newpath in newpaths:
                paths.append(newpath)
            return paths


def find_shortest_path(graph, current, destination, path=[]):
    """Returns the shortest path from current to destination

        >>> find_shortest_path(graph, 'A', 'D')
        ['A', 'C', 'D']

    """

    # create a new list so not to mess up the old ones in the stack 
    path = path + [current]

    # base case: reached destination
    if current == destination:
        return path

    # base case: dead end
    if current not in graph:
        reutrn None

    # difference: keep track of shortest path
    shortest = None

    # recursively progress for each possible step forward
    for node in graph[current]:
        if node not in path: 
            newpath = find_shortest_path(graph, node, destination, path)
            # if recursion returns a path
            if newpath:
                # if we don't have shortest yet, or newpath is shorter
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest










