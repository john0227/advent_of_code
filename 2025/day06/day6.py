import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = [line for line in file.read().split("\n") if line]
    numbers = [list(map(int, line.strip().split())) for line in lines[:-1]]
    operations = lines[-1].strip().split()

def calc(numbers: list[list[int]], operations: list[str]) -> int:
    res = 0
    for i, op in enumerate(operations):
        f = (lambda a, b: a * b) if op == "*" else (lambda a, b: a + b)
        r = 1 if op == "*" else 0
        for row in numbers:
            r = f(r, row[i])
        res += r
    return res

print(calc(numbers, operations))
