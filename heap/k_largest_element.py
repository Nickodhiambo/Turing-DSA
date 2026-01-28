#!/usr/bin/env python

# We use a heap to maintaim k elements, starting from the largest
# We loop through the input list, adding an item to the heap# We check if heap exceeds required size k, in which case we pop the latest entrant
# By the time we finish looping, the k largest element will be at the top of the heap
# return the element

import heapq

def k_largest_element(arr: list[int], k: int) -> int:
    # Edge case: Empty list
    if not arr:
        return 0

    # Maintain a heap of k elements
    heap: list[int] = []

    # Loop through input, add every item to heap
    for item in arr:
        heapq.heappush(heap, item)
        # Pop from heap if k size exceeded
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

if __name__ == '__main__':
    print(k_largest_element([3,2,1,5,6,4], 2))

