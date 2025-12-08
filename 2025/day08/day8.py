import heapq
import sys


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def dist_key(p1: "Point", p2: "Point"):
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


class UFDS:
    def __init__(self, n):
        self.roots = list(range(n))
        self.sizes = [1] * n
        self.groups = n

    def find(self, x: int) -> int:
        r = self.roots[x]
        while self.roots[r] != r:
            r = self.roots[r]
        while self.roots[x] != r:
            x, self.roots[x] = self.roots[x], r
        return r

    def unify(self, x: int, y: int) -> bool:
        r1 = self.find(x)
        r2 = self.find(y)
        if r1 == r2:
            return False

        if self.sizes[r1] < self.sizes[r2]:
            r1, r2 = r2, r1
        self.roots[r2] = r1
        self.sizes[r1] += self.sizes[r2]
        self.sizes[r2] = 0
        self.groups -= 1
        return True


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split()
    points = [Point(*map(int, line.split(","))) for line in lines]

Heap = list
def sort_by_weights(points: list[Point]) -> Heap:
    n = len(points)
    heap = []
    for i in range(n - 1):
        p1 = points[i]
        for j in range(i + 1, n):
            p2 = points[j]
            heap.append((Point.dist_key(p1, p2), i, j))
    heapq.heapify(heap)
    return heap

def kruskal(n: int, edges: Heap):
    ufds = UFDS(n)
    while edges:
        _, i, j = heapq.heappop(edges)
        if not ufds.unify(i, j):
            continue
        if ufds.groups == 1:
            return i, j
    return -1, -1

edges = sort_by_weights(points)
i, j = kruskal(len(points), edges)

p1, p2 = points[i], points[j]
print(p1.x * p2.x)
