#!/usr/bin/env python

"""
Checks if pairs of input parenthesis are valid. For valid
pairs, all pairs match, and inner pairs close before outer
pairs.
Returns a boolean
"""

# Plan
# We use a combination of hash set and stack data structures
# Hash set matches closing bracket to opening to help us
# determine if a closing bracket is matched with the last opening
# Stack tracks the latest opening bracket such that when
# The next bracket is a closing one we check if it matches
# with the last opening bracket

def valid_parenthesis(s: str) -> bool:
    # Edge case: Empty input string
    if not s:
        return False

    # Hash set to match closing to opening
    mapping = {')': '(', '}': '{', ']': '['}

    # Stack to track latest opening bracket
    stack = []

    # Loop through every string character in input
    for char in s:
        if char in mapping: # char is a closing bracket
            corresponding_opening = stack.pop() if stack else '#'
            # Match the opening to closing
            if corresponding_opening != mapping[char]:
                return False
        else: # char is an opening bracket
            stack.append(char)

    # If stack is empty by end of loop, all brackets match
    return not stack

if __name__ == '__main__':
    print(valid_parenthesis('(([]))'))
    print(valid_parenthesis('(])'))
    print(valid_parenthesis(''))
