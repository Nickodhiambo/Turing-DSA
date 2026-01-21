#!/usr/bin/env python

# reverse entire array
# reverse the first k
# Reverse k+1 to the end

def rotate_array(arr: list[int], k: int) -> list[int]:
    n: int = len(arr)

    # Avoid unnecessary rotations which happen when
    # k is equal to or bigger than array size
    k = k % n

    if k == n:
        return arr

    # Reverse entire array
    arr[:] = arr[::-1]
    # Reverse first k
    arr[:k] = arr[:k][::-1]
    # Reverse remaining n-k
    arr[k:] = arr[k:][::-1]

    return arr

if __name__ == '__main__':
    print(rotate_array([1,2,3,4,5,6,7], 7))
