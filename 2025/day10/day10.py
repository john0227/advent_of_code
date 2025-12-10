from collections import deque
import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")
    lights = []
    buttons = []
    joltages = []
    for line in lines:
        items = line.split()

        light = 0
        for i, c in enumerate(items[0].strip("[]")):
            if c == "#":
                light |= 1 << i
        lights.append(light)

        button = []
        for scheme in items[1:-1]:
            b = 0
            for i in map(int, scheme.strip("()").split(",")):
                b |= 1 << i
            button.append(b)
        buttons.append(button)

        joltages.append(list(map(int, items[-1].strip("{}").split(","))))

def bfs(light: int, buttons: list[int]):
    dq = deque([0])
    seen = {0}
    min_presses = 0
    while dq:
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr == light:
                return min_presses
            for scheme in buttons:
                next = curr ^ scheme
                if next not in seen:
                    dq.append(next)
                    seen.add(next)
        min_presses += 1
    return 0

ans = 0
for l, b, j in zip(lights, buttons, joltages):
    ans += bfs(l, b)
print(ans)
