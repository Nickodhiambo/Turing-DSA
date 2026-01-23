#!/usr/bin/env python

def max_subsequence(arr: list[int]) -> int:
    # The sum of all positive numbers in an array guarantees the maximum subsequence
    # Edge case: Empty array
    if not arr:
        return 0
    # Edge case: all items are negative
    if all(num < 0 for num in arr):
        return max(arr)
    # Else, sum only positive numbers
    return sum(num for num in arr if num > 0)

if __name__ == '__main__':
    print(max_subsequence([1,2,3,4]))
    print(max_subsequence([]))
    print(max_subsequence([1,-1,1,-1]))
    print(max_subsequence([-1,-1,-1]))
