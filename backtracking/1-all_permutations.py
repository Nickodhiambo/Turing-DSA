#!/usr/bin/env python

def permutations(arr: list[list[int]]):
    result = []
    def backtrack(i):
        # base case: Full permutation reached
        if i == len(arr):
            result.append(arr[:])
            return
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            backtrack(i+1)
            arr[i], arr[j] = arr[j], arr[i]
    backtrack(0)
    return result

if __name__ == '__main__':
    print(permutations([1,2,3]))
