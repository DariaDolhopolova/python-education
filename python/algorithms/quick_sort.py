"""This module implements iterative version of quick sort with functions:
partition() - supportive function for pivot
quick_sort_iter() - function for quick sort"""

def partition(arr, low, high):
    """Places pivot at the right position and all smaller elements to the left of it."""
    i = low - 1
    last = arr[high]

    for j in range(low, high):
        if arr[j] <= last:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_iter(arr, low, high):
    """Implements quick sort, sorting all the elements to the right and left of the pivot"""
    size = high - low + 1
    stack = [0] * size
    top = -1
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        pivot = partition(arr, low, high)
        if pivot - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1
        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high


array = [4, 3, 5, 2, 1, 3, 2, 3]
LENGHT = len(array)
quick_sort_iter(array, 0, LENGHT - 1)
print("Sorted array is:")
for num in range(LENGHT):
    print("% d" % array[num])
