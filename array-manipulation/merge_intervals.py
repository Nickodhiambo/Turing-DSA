#!/usr/bin/env python

#loop over a list of intervals
# We compare end interval of the current with
#start of the next. If current[end] > next[start] 
#adjust the end interval of current
# Else, add current interval to output list and set next as
#current

def merge_intervals(intervals: list[list]) -> list[list]:
    # Handle edge case
    if not intervals:
        return []
    # Sort intervals by start as key
    intervals.sort(key=lambda x: x[0])
    result = [] # Output list
    current_interval = intervals[0]

    # Loop through intervals
    for interval in intervals[1:]:
        if current_interval[1] >= interval[0]:
            current_interval[1] = interval[1]
        else:
            result.append(current_interval)
            current_interval = interval
    result.append(current_interval)
    return result

if __name__ == '__main__':
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
