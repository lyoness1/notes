"""Bubble Sort"""

def bubble_sort(arr):
    """Returns sorted arr

        >>> bubble_sort([4, 6, 2, 0, 10])
        [0, 2, 4, 6, 10]

    """

    # move through list first time
    for i in range(len(arr)):
        # move through list second time
        for j in range(len(arr)-1):
            # if out of order, switch
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Analysis: O(n^2)

def better_bubble_sort(arr):
    """Returns sorted arr

        >>> better_bubble_sort([4, 6, 2, 0, 10])
        [0, 2, 4, 6, 10]

    """

    # move through list first time
    for i in range(len(arr)-1):
        # move through list second time (only until already sorted)
        for j in range(len(arr)-1-i):
            # if out of order, switch
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Analysis: O(n^2) still, even with half the looping inside


def win_fast_bubble(arr):
    """Returns sorted arr

        >>> win_fast_bubble([4, 6, 2, 0, 10])
        [0, 2, 4, 6, 10]

    """

    # move through list first time
    for i in range(len(arr)-1):
        # keep track of if swap made
        made_swap = False
        # move through list second time (only until already sorted)
        for j in range(len(arr)-1-i):
            # if out of order, switch
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                made_swap = True
                # if nothing was swapped, list is already sorted!
                if not made_swap:
                    break

    return arr

# Analysis: O(n^2) still, but pessimistically


def merge_sort(arr):
    """Returns sorted arr by dividing, sorting (at len 1), and merging.

        >>> merge_sort([4, 6, 2, 0, 10])
        [0, 2, 4, 6, 10]

    """

    # base case: list is one long, which is sorted
    if len(arr) < 2:
        return arr

    # divide list in half
    mid_index = len(arr) / 2
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]

    # sort each half
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # initialize output list
    merged_arr = []
    
    # merge sorted sublists
    while left_arr or right_arr:
        
        # if one list is empty, extend the remaining list to output
        if not left_arr:
            merged_arr.append(right_arr.pop(0))
        elif not right_arr:
            merged_arr.append(left_arr.pop(0))

        # if items in both lists, remove smaller first item and append to output
        elif left_arr[0] < right_arr[0]:
            merged_arr.append(left_arr.pop(0))
        else:
            merged_arr.append(right_arr.pop(0))
        
    return merged_arr

# Analysis: 
# Runtime: O(lg(n)) for dividing to sort, O(n) to merge --> O(nlg(n))
# Space: O(n) additional space used for callstack length of original list


def quick_sort(arr):
    """Chose pivot, sort around pivot, sort sublists.

        >>> quick_sort([4, 6, 13, 2, 0, 10])
        [0, 2, 4, 6, 10, 13]

    """

    print "sorting: ", arr

    # base case:
    if len(arr) < 2:
        print "returning: ", arr
        return arr

    pivot_idx = 0
    checking_idx = 1

    # loop all the way through list with right_idx
    while checking_idx < len(arr):
        print "checking %s against pivot %s"%(arr[checking_idx], arr[pivot_idx])
        # if an element encountered is less than pivot, move it back to to_place
        # increment to_place to position right of elements less than pivot
        # (this is where the pivot will end up after passing through entire arr)
        if arr[checking_idx] < arr[pivot_idx]:
            print "moving %s to left of pivot"%(arr[checking_idx])
            to_move = arr.pop(checking_idx)
            arr.insert(pivot_idx, to_move)
            pivot_idx += 1
            print arr
        # continue checking rest of list
        checking_idx += 1


    print "sublist has been sorted around pivot %i: "%(arr[pivot_idx]), arr

    # now all elements left of pivot are smaller, all elements after are larger
    # call self recursively on left and right segments, not including pivot
    quick_sort(arr[:pivot_idx])
    quick_sort(arr[pivot_idx+1:])

    return arr

# Analysis: doesn't work. try using helper fn. 





















if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"


