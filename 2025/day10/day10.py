import numpy as np
import cvxpy as cp
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
            button.append(list(map(int, scheme.strip("()").split(","))))
        buttons.append(button)

        joltages.append(list(map(int, items[-1].strip("{}").split(","))))

def solve(buttons: list[list[int]], target_joltage: list[int]) -> int:
    """
    GIVEN:
        buttons        := (n x m) matrix
        target_joltage := (1 x m) matrix

        where n := number of buttons
              m := number of lights

    FIND:
        x := (n x 1) matrix, such that
            Ax = b

        where
            A = buttons.T
            b = target_joltage.T
            sum(x) is minimized
    """
    button_mat = []
    for scheme in buttons:
        row = [0] * len(target_joltage)
        for i in scheme:
            row[i] += 1
        button_mat.append(row)

    button_mat = np.matrix(button_mat).T
    target_mat = np.matrix(target_joltage)

    # ILP solver
    n = button_mat.shape[1]
    x = cp.Variable(n, integer=True, nonneg=True)
    objective = cp.Minimize(cp.sum(x))
    constraints = [ button_mat @ x == target_mat ]
    prob = cp.Problem(objective, constraints)
    prob.solve()

    if isinstance(x.value, np.ndarray):
        return int(x.value.sum())
    return 0

ans = 0
for l, b, j in zip(lights, buttons, joltages):
    ans += solve(b, j)
print(ans)
