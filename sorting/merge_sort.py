def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) or j < len(right):
            if i >= len(left):
                arr[k] = right[j]
                j += 1
            elif j >= len(right):
                arr[k] = left[i]
                i += 1
            elif left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            elif left[i] >= right[j]:
                arr[k] = right[j]
                j += 1
            k += 1

if __name__ == '__main__':
    alist = [6, 3, 4, 5, 2, 1, 2]
    print(f'Before: {alist}')
    merge_sort(alist)
    print(f'After: {alist}')

