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
    shapes.sort(key=lambda shape: sum(1 for row in shape for val in row if val == "."))

    # list of ((n, m), (..quantity of each shape))
    regions = []
    while lines:
        dim, num_shapes = lines.pop().split(": ")
        w, h = map(int, dim.split("x"))
        num_shapes = list(map(int, num_shapes.split()))
        regions.append(((w, h), num_shapes))

    return shapes, regions

def get_rotations(shapes: list[list[list[str]]]):
    rotations = []
    for shape in shapes:
        rotations.append([])
        rot = [
            [[int(shape[r][c] == "#") << (2 - c) for c in range(3)] for r in range(3)],
            [[int(shape[r][c] == "#") << r for r in range(2, -1, -1)] for c in range(3)],
            [[int(shape[r][c] == "#") << c for c in range(2, -1, -1)] for r in range(2, -1, -1)],
            [[int(shape[r][c] == "#") << (2 - r) for r in range(3)] for c in range(2, -1, -1)],
        ]

        seen = set()
        for r in rot:
            rkey = tuple(sum(row) for row in r)
            if rkey not in seen:
                rotations[-1].append(list(rkey))
                seen.add(rkey)
    return rotations

def can_fill_region(region, rotations) -> bool:
    def empty_points(grid):
        # subtract 2 to only get empty points that we can place shapes on
        #   -> shapes are all 3x3
        return [(r, c) for r in range(rows - 2)
                       for c in range(cols - 2)
                       if grid[r] & (1 << (cols - c - 1)) == 0]

    def can_place_shape(r, c, grid, shape):
        return grid[r]     & (shape[0] << (cols - c - 3)) == 0 and \
               grid[r + 1] & (shape[1] << (cols - c - 3)) == 0 and \
               grid[r + 2] & (shape[2] << (cols - c - 3)) == 0

    def fill_shape(r, c, grid, shape):
        grid[r]     |= shape[0] << (cols - c - 3)
        grid[r + 1] |= shape[1] << (cols - c - 3)
        grid[r + 2] |= shape[2] << (cols - c - 3)

    def remove_shape(r, c, grid, shape):
        grid[r]     ^= shape[0] << (cols - c - 3)
        grid[r + 1] ^= shape[1] << (cols - c - 3)
        grid[r + 2] ^= shape[2] << (cols - c - 3)

    def backtrack(i, scheme, grid, rotations, seen):
        if i == len(scheme):
            return True

        rot_idx = scheme[i]
        for r, c in empty_points(grid):
            for rotation in rotations[rot_idx]:
                if can_place_shape(r, c, grid, rotation):
                    fill_shape(r, c, grid, rotation)
                    seenkey = tuple(grid), i
                    if not seenkey in seen:
                        seen.add(seenkey)
                        if backtrack(i + 1, scheme, grid, rotations, seen):
                            return True
                    remove_shape(r, c, grid, rotation)
        return False

    (cols, rows), shapes = region
    grid = [0 for _ in range(rows)]

    scheme = []
    for i, num in enumerate(shapes):
        scheme.extend([i] * num)
    return backtrack(0, scheme, grid, rotations, set())

shapes, regions = read_content(lines)
rotations = get_rotations(shapes)

ans = 0
for region in regions:
    can_fill = can_fill_region(region, rotations)
    if can_fill:
        ans += 1
print(ans)
