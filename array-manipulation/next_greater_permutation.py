#!/usr/bin/env python

# Find the dip
# swap number at the dip with smallest number to the
# right of it
# rearrange the numbers after the deep to the right in
# ascending order

def next_greater_permutation(arr: list[int]) -> list[int]:
    # Edge case: Empty input array
    if not arr:
        return []
    # Find the dip: point from the right where array is
    # descending
    n = len(arr)
    i = n - 2

    # Find the dip
    while arr[i] >= arr[i+1]:
        i -= 1
    # Swap the number at dip with smallest greater no to
    # the right
    if i >= 0:
        j = n - 1
        while i < j and arr[i] >= arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    # rearrange numbers from dip to right in ascending
    arr[i+1:] = arr[i+1:][::-1]
    return arr

if __name__ == '__main__':
    print(next_greater_permutation([1,2,3]))
    print(next_greater_permutation([1,3,5,2,4]))
    print(next_greater_permutation([1,3,5,4,2]))

