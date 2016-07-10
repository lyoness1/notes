"""Counting Sort"""

def counting_sort(to_sort_list, max_value):
    """Sorts the list time efficiently, space inefficiently"""

    # list of 0's at indecies 0 to max_value
    # this will be a 'histogram' of values from original list to sort
    histogram = [0] * (max_value + 1)

    # populate histogram so each index will have a count of times that
    # numer occurs in the original list. Ex: [1, 2, 3, 3] -> [0, 1, 1, 2]
    for item in to_sort_list:
        histogram[item] += 1

    # instantiate an output list that will be sorted
    sorted_output = []

    # for each item in histogram
    for item, count in enumerate(histogram):
        # for each occurance of the item (will skip the 0s'):
        for time in range(count):
            # add the item to sorted list
            sorted_output.append(item)

    return sorted_output


# ANALYSIS

# Runtime: O(n). Linear to create histogram, linear to go through nested for's.
# The first for loops over each UNIQUE item, and the inner loops for each 
# occurange of each item, so it's really just going over n things again from
# the original list. Just in two steps. 

# Space: O(n) b/c created a new list of length n for the output. 