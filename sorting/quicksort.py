# Worst case: O(n^2)
# Best case: O(nlogn)
# Average case: O(nlogn)
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


# While the undivided array has more than one element:
# The array is partitioned, with the partition ending in it's sorted place
# The array is recursively split around the partition
def quick_sort_helper(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        quick_sort_helper(arr, l, q - 1)
        quick_sort_helper(arr, q + 1, r)


# CLRS style partition:
# How it works:
# partition element is last element in array
# j moves across array until r-1.
# When elements with value less than partition are found,
# i is incremented, and swapped with j
# i maintains the position of the last element with value
# less than partition.
# When j hits the element before the partition (r - 1),
# the partition is swapped with i + 1 (the first value greater than partition).
# The partition is now in it's final place, and it's index is returned
def partition(arr, l, r):
    partition_value = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= partition_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


# Optimizations:
# Partition selection: median of 3 (first, last middle) becomes partition
# Shuffle the array at each split
# For small arrays revert to insertion sort
# Minimize recursion stack space: recurse on smaller side first

if __name__ == '__main__':
    alist = [4, 2, 5, 9, 1, 3, 4, 10, 3, 20]
    print(f'Before: {alist}')
    quick_sort(alist)
    print(f'After: {alist}')
