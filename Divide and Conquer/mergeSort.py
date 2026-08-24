"""
Author: Juan David Bernal Maldonado
Date (DD/MM/YY): 09/08/26
"""

def mergeSort(arr, low, high):
    if low + 1 < high:
        mid = (low + high) // 2
        linv = mergeSort(arr, low, mid)
        rinv = mergeSort(arr, mid, high)
        # merge two sorted halves
        inv = merge(arr, low, mid, high)
        ans = linv + rinv + inv
    else: ans = 0
    return ans 

def merge(arr, low, mid, high):
    tmp = [0] * len(arr)
    # make a copy of current segment
    for i in range(low, high): 
        tmp[i] = arr[i]
    # iterators for tmp
    l, r = low, mid
    inv = 0
    # n will iterate on arr
    for n in range(low, high):
        # l has reached the end of the left half
        if l == mid:
            arr[n], r = tmp[r], r + 1
        # r has reached the end of the right half
        elif r == high:
            arr[n], l = tmp[l], l + 1
        else:
            # choose left
            if tmp[l] <= tmp[r]:
                arr[n], l = tmp[l], l + 1
            # choose right
            else:
                arr[n], r = tmp[r], r + 1
                # count inversions
                inv += mid - l
    return inv

A = [3, 2, 4, 1]
print(mergeSort(A, 0, len(A)))
print(A)