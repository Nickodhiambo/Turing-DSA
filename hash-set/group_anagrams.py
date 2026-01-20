#!/usr/bin/env python

#Go through the input list
    # rearrange the word
    #Add it to hash set with similar words
# Loop through the hash set, return values of keys, each
# value as separate list

from collections import defaultdict

def group_anagrams(strs: list[str]):
    anagrams_dict: dict[str, list] = defaultdict(list)

    result = [] # Will store anagrams
    for s in strs:
        # sort string
        sorted_s = ''.join(sorted(s))
        anagrams_dict[sorted_s].append(s)
    return list(anagrams_dict.values())

if __name__ == '__main__':
    input_str = ['eat', 'tea', 'ate', 'tan', 'nat', 'bat']
    print(group_anagrams(input_str))
