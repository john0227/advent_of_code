import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")
    points = [list(map(int, line.split(","))) for line in lines]

def find_largest_rect(points: list[list[int]]) -> int:
    n = len(points)
    maxarea = 0
    for i in range(n - 1):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            maxarea = max(maxarea, area)
    return maxarea

print(find_largest_rect(points))
