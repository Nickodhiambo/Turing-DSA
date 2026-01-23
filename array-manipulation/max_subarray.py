#!/usr/bin/env python

# Naive solution
# Generate all subarrays
# For each subarray, sum it, and check if it's maximum
# seen so far.
# if it is, update maximum
# return maximum

def maximum_subarray(arr: list[int]) -> int:
    # Edge case: empty input
    if not arr:
        return 0

    max_sum = 0
    # Generate all subarrays
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == '__main__':
    print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))

