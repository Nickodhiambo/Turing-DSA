#!/usr/bin/env python

#  What is the frequency of items in the input list?
# We need a min-heap to sort frequencies
# Loop through frequencies adding each frequency to the heap# With every addition, check if heap size exceeds k
    # if it does, remove the topmost element
# return a list containing k frequent

import heapq
from collections import Counter

def top_k_most_frequent(arr: list[int], k: int) -> list[int]:
    # Get frequencies of items in input list
    freq: dict[int, int] = Counter(arr)

    # A heap where every item is tuple(freq, item)
    heap: list[tuple] = []

    # Loop through the frequency dict adding items to heap
    for item, count in freq.items():
        # We want to maintain the heap by count
        heapq.heappush(heap, (count, item))
        # To guarantee only top k elements are stored
        # in heap, be removing the topmost frequency
        # whenever k is exceeded
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap[::-1]]

if __name__ == '__main__':
    print(top_k_most_frequent([1,1,1,2,2,3], 2))
