#!/usr/bin/env python

# Initial case: Check if starting window of s is an anagram of p
# slide s, one char at a time. for every sliding run, we are
# removing leftmost char, adding the next char in string s and checking if current window is an anagram of s
# simply return a list of starting indices of every anagram of p in s

from collections import Counter

def anagrams_of_p_in_s(s: str, p: str) -> list[int]:
    # edge case: s is shorter than p
    if len(s) < len(p):
        return 0
    # Initialize output list to store anagram indices
    result: list[int] = []
    # We know that a given window is an anagram of p if it has the same character count as p
    p_count = Counter(p)
    s_count = Counter(s[0:len(p)])

    # Check if initial window matches
    if p_count == s_count:
        result.append(0)

    # Slide the window
    for i in range(len(p), len(s)):
        # Remove leftmost char
        left_char = s[i - len(p)]
        s_count[left_char] -= 1

        if s_count[left_char] < 1:
            del s_count[left_char]

        # add rightmost char
        right_char = s[i]
        s_count[right_char] = s_count.get(right_char, 0) + 1
        # check if new window matches
        if p_count == s_count:
            result.append(i - len(p) + 1)
    return result

if __name__ == '__main__':
    print(anagrams_of_p_in_s('cbaebabacd', 'abc'))
