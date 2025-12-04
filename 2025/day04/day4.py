from collections import deque
import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    input = file.read().split()
    grid = []
    for row in input:
        grid.append(list(row))

def forklift_access_points(grid) -> int:
    n, m = len(grid), len(grid[0])

    dq = deque()
    pts = set()
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "@":
                dq.append((r, c))
                pts.add((r, c))

    adds = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    access_pts = 0
    while dq:
        pt = r, c = dq.popleft()
        pts.discard(pt)
        # if the point was already removed
        if grid[r][c] != "@":
            continue

        adj, adjs = 0, []
        for radd, cadd in adds:
            pt = rr, cc = r + radd, c + cadd
            if 0 <= rr < n and 0 <= cc < m and grid[rr][cc] == "@":
                adj += 1
                if pt not in pts:
                    adjs.append(pt)

        if adj < 4:
            grid[r][c] = "x"
            dq.extend(adjs)
            pts.update(adjs)
            access_pts += 1
    return access_pts

ans = forklift_access_points(grid)
print(ans)
