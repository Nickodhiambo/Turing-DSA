#!/usr/bin/env python

def maximum_subarray_sum(arr: list) -> int:
    # Initialize trackers for the maximum sum found
    # and sum of current subarray
    max_sum, curr_sum = 0, 0

    for num in arr: 
        # Current sum is obtained by adding the next number in the array to current value
        curr_sum += num
        # Either continue adding the next number to the current sum or start a new current sum
        curr_sum = max(curr_sum, num)
        # Update max every time we have a new current sum
        max_sum = max(max_sum, curr_sum)

    return max_sum

if __name__ == '__main__':
    print(maximum_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))

