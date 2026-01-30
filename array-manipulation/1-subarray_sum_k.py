#!/usr/bin/env python

def subarray_sum_equals_k(arr: list[int], k: int) -> int:
    if not arr:
        return 0
    # Prefix sum to store cummulative sums
    prefix_sum: dict[int, int] = {0 : 1}
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num
        # Update count if cumulative sum adding upto the current index is equal to k
        count += prefix_sum.get((current_sum - k), 0)
        # Update frequency of current sum
        prefix_sum[current_sum] = prefix_sum.get(
                current_sum, 0) + 1
    return count

if __name__ == '__main__':
    print(subarray_sum_equals_k([1,1,1], 2))
