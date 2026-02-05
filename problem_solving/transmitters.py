#!/usr/bin/env python

"""
This is a greedy algorithm that purposes to place minimun number of radio transmitters on houses arranged in order so all houses are effectively covered
"""

# Plan
# Sort houses in ascending
# Start at the leftmost house and move as a far right as
# possible within range k
# Place a transmitter at last house within k.
# Skip all houses already covered
# Repeat until all houses are covered

def minimum_transmitters(houses: list[int], k: int) -> int:
    # Edge case: No houses
    if not houses:
        return 0
    # Sort houses
    houses.sort()

    i, n, transmitters = 0, len(houses), 0

    while i < n: # While there are still hse to cover
        # Leftmost uncovered house
        start = houses[i]
        # Move right within k
        while i < n and houses[i] <= start + k:
            i += 1
        # Place a transmitter at last hse within k
        transmitter_pos = houses[i-1]
        transmitters += 1

        # Skip all covered houses by this transmitter
        while i < n and houses[i] <= transmitter_pos + k:
            i += 1
    return transmitters

if __name__ == '__main__':
    print(minimum_transmitters([1,3,5,7,11], 3))
    print(minimum_transmitters([1,2,3,5,9], 1))
