#!/usr/bin/env python

"""
Input is a partially almost sorted array. The array can be
Sorted by either swapping two items or reversing a section
Sorting by swapping takes precedence if array can be sorted by both
Print out statements if array can be sort either way, or cannot be sorted
"""

# Plan
# sort input array to determine if array can be
# Sorted by swapping or reversing
# Handle sorting by swapping
# Handle sorting by reversing
# Handle cannot be sorted

def almost_sorted(arr: list[int]):
    sorted_arr = sorted(arr)

    # Determine places where the two arrays differ
    diff = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]

    # If diff lengtg is exactly 2, array should be sorted by swapping
    if len(diff) == 2:
        l, r = diff[0], diff[1]
        arr[l], arr[r] = arr[r], arr[l]
        print('Yes')
        print(f'swap {l+1} {r+1}')
        return

    l, r = diff[0], diff[-1]
    if arr[l:r+1][::-1] == sorted_arr[l:r+1]:
        arr[l:r+1][::-1]
        print('Yes')
        print(f'reverse {l+1} {r+1}')
        return
    print('No')

if __name__ == '__main__':
    print(almost_sorted([1,3,2,4,5]))
    print(almost_sorted([1,4,3,2,5]))
    print(almost_sorted([1,2,6,5,4,3,7]))
    print(almost_sorted([1,4,2,5,3,6]))
