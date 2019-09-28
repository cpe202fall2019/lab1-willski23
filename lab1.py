def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    # checks to see if list is greater than zero before finding max value
    if int_list == None:
        raise ValueError("No values in list")
    if len(int_list) == 0:
        return None
    max_val = int_list[0]
    for i in range(1, len(int_list)):
        if int_list[i] > max_val:
            max_val = int_list[i]
    return max_val


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    # base case = end of list
    if int_list == None:
        raise ValueError("No Values in list")
    if len(int_list) == 0:
        return int_list
    # probably need another exception
    return int_list[-1:] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

    if int_list == None:
        raise ValueError('No Values in List')
    if len(int_list) == 0:
        return None
    mid = (low + high) // 2
    if int_list[mid] == target:
        return mid
    # if no target is found by end of list
    if mid == high and mid == low:
        return None
    if int_list[mid] < target:  # mid becomes new low
        return bin_search(target, mid + 1, high, int_list)
    # target is less than mid value : mid becomes new high
    return bin_search(target, low, mid - 1, int_list)