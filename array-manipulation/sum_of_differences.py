#!/usr/bin/env python

"""
Sums the differences of numbers in lists at corresponding
positions and returns the total
Takes a list of lists as input. The sublists are of equal length
"""

# Plan
# A total to accumulate sum of differences
# Loop through every sublist. 
# For every sublist, add the sum of differences of numbers
# In corresponding positions with the rest of the sublists
# after it to the total
# Return total

def sum_of_differences(arr: list[list[int]]) -> int:
    # Edge case: Empty array
    if not arr:
        return 0

    # Total to accumulate sums of differences
    total = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for dgt1, dgt2 in zip(arr[i], arr[j]):
                total += abs(dgt1 - dgt2)
    return total

if __name__ == '__main__':
    print(sum_of_differences([[1,2,3], [4,5,6]]))

