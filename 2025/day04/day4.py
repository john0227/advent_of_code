import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    input = file.read().split()
    grid = []
    for row in input:
        grid.append(list(row))

def forklift_access_points(grid) -> int:
    n, m = len(grid), len(grid[0])
    adds = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    access_pts = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] != "@":
                continue

            adj = 0
            for radd, cadd in adds:
                rr, cc = r + radd, c + cadd
                adj += int(0 <= rr < n and 0 <= cc < m and grid[rr][cc] == "@")
            access_pts += int(adj < 4)
    return access_pts

ans = forklift_access_points(grid)
print(ans)
