def bin_search(arr, target):
    l = 0
    r = len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] == target:
            return arr[mid]
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1

if __name__ == '__main__':
    alist = [1,4,7,8,9,33,66,199]
    print(alist)
    target = 7
    print(f'Search for {target}: {bin_search(alist, target)}')
    target = 10
    print(f'Search for {target}: {bin_search(alist, target)}')
