"""This module implements binary search using recursion."""


def binary_search(my_list, target, low=None, high=None):
    """This function implements binary search on the sorted list.
    If it cannot find the element it returns -1"""
    if low is None:
        low = 0
    if high is None:
        high = len(my_list) - 1

    if high < low:
        return -1
    midpoint = (low + high) // 2
    if my_list[midpoint] == target:
        return midpoint
    elif target < my_list[midpoint]:
        return binary_search(my_list, target, low, midpoint-1)
    else:
        return binary_search(my_list, target, midpoint+1, high)


if __name__ == "__main__":
    new_list = [2, 4, 7, 10, 12, 18, 45]
    TAR = 18
    print(binary_search(new_list, TAR))
