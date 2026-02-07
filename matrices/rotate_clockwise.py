#!/usr/bin/env python

"""
This algorithm rotates layers of a matrix clockwise in place
"""

# Plan
# Get matrix dimensions
# Loop over all the 4 edges of a the current layer n times,
# With each loop run, you are shifting the items one place
# to the right for top layer, one place left for bottom layer,
# one place down for the right and one place up for left
# Return the rotated matrix

def rotate_clockwise_n(matrix: list[list[int]], n: int) -> list[list[int]]:
    # Handle edge case: Empty input
    if not matrix:
        return matrix

    # Get dimensions
    rows, cols = len(matrix), len(matrix[0])

    # Loop over each layer n times
    for _ in range(n):
        # Get position of current layer
        top, left, bottom, right = 0, 0, rows-1, cols-1

        # Preserve top rightmost value so we recover it
        top_rightmost = matrix[0][cols-1]

        # Rotate top row
        for col in range(right-1, left-1, -1):
            matrix[top][col+1] = matrix[0][col]

        # Rotate bottom row
        for col in range(1, right):
            matrix[bottom][col-1] = matrix[bottom][col]

        # Rotate left col
        for row in range(1, bottom):
            matrix[row-1][left] = matrix[row][left]

        # Rotate right col
        for row in range(bottom-1, top-1, -1):
            matrix[row+1][right] = matrix[row][right]

        matrix[1][right] = top_rightmost

        # Move to inner layers
        top += 1
        left += 1
        bottom -= 1
        right -= 1
    # Return matrix
    return matrix

if __name__ == '__main__':
    matrix =  [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
    print(rotate_clockwise_n(matrix, 1))
