#!/usr/bin/env python

# Plan
# We use a heap data structure to store meeting ending
# times. This guarantees the shortest ending time would be
# at the top
# We sort the intervals in ascending order by starting time
# and loop through each interval. For the current interval 
# if it's overlapping with the shortest meeting, it means we
# would need an extra room, so we add it to heap
# If it's not, it means rooms could be shared, so we remove
# the smallest ending meeting from heap
# We return heap length which is equal to number of rooms

import heapq

def meeting_rooms(intervals: list[list[int]]) -> int:
    # Edge case: empty intervals
    if not intervals:
        return 0

    # Sort intervals by starting time
    intervals.sort(key=lambda x: x[0])

    # Heap to store ending times
    ending_times = []

    for interval in intervals:
        # No overlap, meeting rooms could be shared
        if ending_times and ending_times[0] <= interval[0]:
            heapq.heappop(ending_times)
        # Overlap. we need a new room
        heapq.heappush(ending_times, interval[1])
    return len(ending_times)

if __name__ == '__main__':
    print(meeting_rooms([[0,30], [5,10], [15,20]]))
