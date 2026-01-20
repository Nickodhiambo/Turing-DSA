#!/usr/bin/env python

#Left and right boundaries of window are fixed at
#the beginning
# A tracker that watches for the biggest window of
#unique chars seen so far
#Visit  every char of the input str once, adding it to
# the window
# With every addition check if char is repeating:
# if it is:
# Move the left boundary forward by 1, else, continue
# to slide right boundary
# return the tracker

from collections import defaultdict

def longest_substring(s: str) -> int:
    l, r = 0, 0
    longest = 0

    counter: dict[str, int] = defaultdict(int)

    for r in range(len(s)):
        counter[s[r]] += 1
        if counter[s[r]] > 1:
            counter[s[r]] -= 1
            l += 1
        longest = max(r - l + 1, longest)
    return longest

if __name__ == "__main__":
    print(longest_substring("abcabcbb"))
    print(longest_substring("aaaaaaa"))
