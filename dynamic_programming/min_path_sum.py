#!/usr/bin/env python

# The cost of path to a cell is the sum of previous vertical and horizontal cell weights
# We'll calculate the cost sum to first row and first col asthe use the result as initial cost paths for subsequent columns

def mimimum_path_sum(grid: list[list]) -> int:
    # edge case: empty grid
    if not grid:
        return 0
    # We need a copy of grid which holds minimum cost path to every cell instead of individual weight of a cell
    rows, cols = len(grid), len(grid[0])
    # Initialize to 0
    dp: list[list[int]] = [[0] * cols for _ in range(rows)]

    # Minimum cost to cell 0,0 is same as cell value of that cell
    dp[0][0] = grid[0][0]

    # Calculate minimum cost to row 1 and col 1
    for n in range(1, cols):
        dp[0][n] = dp[0][n-1] + grid[0][n]
    for m in range(1, rows):
        dp[m][0] = dp[m-1][0] + grid[m][0]

    # Calculate minimum cost to subsequent rows and cols
    for m in range(1, rows):
        for n in range(1, cols):
            dp[m][n] = min(
                    dp[m-1][n], dp[m][n-1]) + grid[m][n]
    return dp[rows-1][cols-1]

if __name__ == '__main__':
    print(mimimum_path_sum([[1,3,1], [1,5,1], [4,2,1]]))
