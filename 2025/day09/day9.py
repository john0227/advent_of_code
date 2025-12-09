import sys


memo = {}

fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")
    polygon = [list(map(int, line.split(","))) for line in lines]

def is_point_inside(point: list[int], polygon: list[list[int]]) -> bool:
    global memo
    if tuple(point) in memo:
        return memo[tuple(point)]

    n = len(polygon)
    px, py = point
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # if point lies on a segment, the point is in polygon by default
        if (px == x1 == x2 and min(y1, y2) <= py <= max(y1, y2)) or \
           (py == y1 == y2 and min(x1, x2) <= px <= max(x1, x2)):
            memo[tuple(point)] = True
            return True

        # if line y=py intersects current edge
        if min(y1, y2) < py <= max(y1, y2):
            if x1 > px:
                inside = not inside

    memo[tuple(point)] = inside
    return inside

def orient(a, b, c):
    '''
    0 → collinear
    1 → clockwise
    -1 → counterclockwise
    '''
    v = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if v > 0: return 1
    if v < 0: return -1
    return 0

def lines_intersect(line: list[list[int]], polygon_edge: list[list[int]]) -> bool:
    A, B = line
    C, D = polygon_edge

    o1 = orient(A, B, C)  # orientation of C wrt AB
    o2 = orient(A, B, D)  # orientation of D wrt AB
    o3 = orient(C, D, A)  # orientation of A wrt CD
    o4 = orient(C, D, B)  # orientation of B wrt CD

    return o1 * o2 < 0 and o3 * o4 < 0

def is_line_inside(line: list[list[int]], polygon: list[list[int]]) -> bool:
    n = len(polygon)
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        if lines_intersect(line, [p1, p2]):
            return False
    return True

def is_rect_inside(point1: list[int], point2: list[int], polygon: list[list[int]]) -> bool:
    x1, y1 = point1
    x2, y2 = point2

    corners = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]

    for i in range(4):
        p1 = corners[i]
        p2 = corners[(i + 1) % 4]
        if not is_point_inside(p1, polygon) or \
            not is_line_inside([p1, p2], polygon):
            return False
    return True

def find_largest_rect(polygon: list[list[int]]) -> int:
    n = len(polygon)
    maxarea = 0
    for i in range(n - 1):
        print(i, end='\r')
        x1, y1 = polygon[i]
        for j in range(i + 1, n):
            x2, y2 = polygon[j]
            pt1 = [min(x1, x2), min(y1, y2)]
            pt2 = [max(x1, x2), max(y1, y2)]
            if is_rect_inside(pt1, pt2, polygon):
                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
                maxarea = max(maxarea, area)
    return maxarea

print(find_largest_rect(polygon))
