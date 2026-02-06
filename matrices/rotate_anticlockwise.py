#!/usr/bin/env python

"""
An algorithm that rotates the layers of a 2D matrix anticlockwise n times and returns the rotated matrix
"""

# Plan
# Get the dimensions of the matrix
# Start with the outer layer and get position of top, left, bottom and right cells
# Rotate outer layer by shifting cells one step to the left
# for the top cells, on step down for left, one step right for
# bottom and one step top for right
# Get the edge positions for the next inner layer and repeat

def rotate_anticlockwise_n(matrix: list[list[int]], n: int) -> list[list[int]]:
    # Edge case empty matrix
    if not matrix:
        return matrix

    # Get dimensions
    rows, cols = len(matrix), len(matrix[0])

    # Rotate matrix n times, moving from outer to inner layers
    for _ in range(n):
        # Get the position of outermost layer
        top, left, bottom, right = 0, 0, rows-1, cols-1

        # Edge case: Preserve value for 0,0 because we erase it when we move top row
        top_left_value = matrix[0][0]

        # Rotate top row
        for col in range(1, cols):
            matrix[top][col-1] = matrix[top][col]
        
        # Rotate right col
        for row in range(1, rows):
            matrix[row-1][right] = matrix[row][right]

        # Rotate bottom row
        for col in range(right-1, left-1, -1):
            matrix[bottom][col+1] = matrix[bottom][col]

        # Rotate left col
        for row in range(bottom-1, top-1, -1):
            matrix[row+1][left] = matrix[row][left]

        # Replace value at [1][0] with the preserved value
        matrix[1][0] = top_left_value

        # Move to inner layer
        top, left, bottom, right = top+1, left+1, bottom-1, right-1
    # Since rotation was in place, return input matrix
    return matrix


if __name__ == '__main__':
    matrix =  [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
    print(rotate_anticlockwise_n(matrix, 2))
