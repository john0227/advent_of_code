import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")

def read_content(lines: list[str]):
    lines = lines[::-1]

    shapes: list[list[list[str]]] = []
    while lines[-1][-1] == ":":
        lines.pop()  # discard line
        # each shape is 3x3
        shapes.append([])
        shapes[-1].append(list(lines.pop()))
        shapes[-1].append(list(lines.pop()))
        shapes[-1].append(list(lines.pop()))
        # discard empty line
        lines.pop()

    # list of ((n, m), (..quantity of each shape))
    regions = []
    while lines:
        dim, num_shapes = lines.pop().split(": ")
        w, h = map(int, dim.split("x"))
        num_shapes = list(map(int, num_shapes.split()))
        regions.append(((w, h), num_shapes))

    return shapes, regions

def can_fill(region, shape_areas):
    (cols, rows), shape_counts = region
    needed_area = sum(shape_areas[i] * count for i, count in enumerate(shape_counts))

    # assume we need 20% more than we actually need
    return (cols * rows) >= int(1.2 * needed_area)


shapes, regions = read_content(lines)
areas = [sum(1 for row in shape for val in row if val == "#") for shape in shapes]

ans = 0
for region in regions:
    ans += int(can_fill(region, areas))
print(ans)
