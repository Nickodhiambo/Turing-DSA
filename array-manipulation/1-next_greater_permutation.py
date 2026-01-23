#!/usr/bin/env python

# Find the dip.The dip is the point from the right where
# the array is descending. It's at that point to the right that we need
# to make changes
# Swap the number at the dip with smallest number
# to the right
# Rearrange numbers to the right of dip in ascending

def next_greater_permutation(arr: list[int]) -> list[int]:
    # Find the dip
    i = len(arr) - 1
    while arr[i-1] >= arr[i]:
        i -= 1
    # Swap number at the dip
    if i >= 0:
        j = len(arr) - 1
        while i < j and arr[i] >= arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    # Rearrange numbers to the right of deep to guarantee
    # the next greater permutation
    arr[i+1:] = arr[i+1:][::-1]
    return arr

if __name__ == '__main__':
    print(next_greater_permutation([1,2,3]))
    print(next_greater_permutation([1,3,2]))
    print(next_greater_permutation([1,3,5,2,4]))

