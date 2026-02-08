#!/usr/bin/env python

def rotate_clockwise(matrix: list[list[int]], n: int) -> list[list[int]]:
    if not matrix:
        return matrix

    rows, cols = len(matrix), len(matrix[0])

    top, left, bottom, right = 0, 0, rows-1, cols-1

    for _ in range(n): # Rotate n times
        top_rightmost = matrix[top][right]

        # Rotate top row
        for col in range(right-1, left-1, -1):
            matrix[top][col+1] = matrix[top][col]

        # Rotate left col
        for row in range(1, bottom+1):
            matrix[row-1][left] = matrix[row][left]

        # Rotate bottom row
        for col  in range(1, right+1):
            matrix[bottom][col-1] = matrix[bottom][col]

        # Rotate right col
        for row in range(bottom-1, top-1, -1):
            matrix[row+1][right] = matrix[row][right]

        matrix[top+1][right] = top_rightmost

        top += 1
        left += 1
        bottom -= 1
        right -= 1
    return matrix

if __name__ == '__main__':
    matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
    print(rotate_clockwise(matrix, 1))
