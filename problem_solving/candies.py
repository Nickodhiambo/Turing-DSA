#!/usr/bin/env python

"""
A greedy algorithm that determine the minimum number of
attempts required to make a target number of candies given
input machines, workers cost per unit of workers and machines and target candies. A candy is a product of machine and
workers and you can buy resources using candies made so far
to maximize output
"""

# Plan
# Check if one pass can achieve desired outcome
# If one pass can't, create candies as long as target is not
# reached. During each production phase, try to balance workers and machines to produce a max number of candies
# Increment the number of production phases through each phase
# Return number of phases

def minimum_candies(m: int, w: int, p: int, n: int) -> int:
    # Can we make target candies by one pass?
    if m * w >= n:
        return 1
    passes = 0
    candies = 0

    while candies < n: # Produce candies as long as we have not reached target
        candies += m * w
        passes += 1

        # Check if we can use candies to maximize prodction resources
        if candies >= p and candies < n:
            # buys is number of resource units we can afford currently
            buys = candies // p
            candies = candies % p

            if m > w: # Increase worker units
                w_add = (m - w // 2) + 1
                buys -= w_add
                # If we can still buy, increase machines
                m += buys
            else: # Increase machine units
                m_add = (w - m // 2) + 1
                buys -= m_add
                w += buys
    return passes

if __name__ == '__main__':
    print(minimum_candies(1,2,1,60))
