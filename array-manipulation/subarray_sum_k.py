#!/usr/bin/env python

# Generate all subarrays
# Sum each subarray and check if it equals k
# Update count

def subarray_sum_equals_k(arr: list[int], k: int) -> int:
    # Edge case: empty list
    if not arr:
        return 0

    count = 0 
    
    # Generate all subarrays
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == k:
                count += 1
    return count

if __name__ == '__main__':
    print(subarray_sum_equals_k([1,1,1], 2))
