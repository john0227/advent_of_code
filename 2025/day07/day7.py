from collections import deque
import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")
    grid = [list(line) for line in lines]

def solve(grid: list[list[str]]) -> int:
    n, m = len(grid), len(grid[0])
    start = grid[0].index("S")
    dp = [[0] * m for _ in range(n)]
    dp[0][start] = 1
    for r, row in enumerate(dp):
        if r == n - 1: break
        for c, count in enumerate(row):
            if dp[r][c] == 0:
                continue
            if grid[r + 1][c] != "^":
                dp[r + 1][c] += count
                continue
            left, right = c - 1, c + 1
            if 0 <= left: dp[r + 1][left] += count
            if right < m: dp[r + 1][right] += count
    return sum(dp[-1])

print(solve(grid))
