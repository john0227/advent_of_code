from collections import deque
import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")
    grid = [list(line) for line in lines]

def solve(grid: list[list[str]]) -> int:
    n, m = len(grid), len(grid[0])
    start = grid[0].index("S")
    dq = deque([start])
    row = 0
    ans = 0
    while row < n - 1:
        visited = set()
        for _ in range(len(dq)):
            curr = dq.popleft()

            if grid[row + 1][curr] != "^":
                if curr not in visited:
                    dq.append(curr)
                    visited.add(curr)
                continue

            ans += 1
            left = curr - 1
            right = curr + 1
            if 0 <= left and left not in visited:
                dq.append(left)
                visited.add(left)
            if right < m and right not in visited:
                dq.append(right)
                visited.add(right)
        row += 1
    return ans

print(solve(grid))
