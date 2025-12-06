import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = [line for line in file.read().split("\n") if line]
    numbers = lines[:-1]
    operations = lines[-1]

def prod(numbers: list[int]):
    res = 1
    for num in numbers:
        res *= num
    return res

def calc(numbers: list[str], operations: str):
    res = 0
    num, nums = '', []
    for c in range(len(numbers[0]) - 1, -1, -1):
        num = ''.join(row[c].strip() for row in numbers)
        if num:
            nums.append(int(num))

        if operations[c] in ("+", "*"):
            res += sum(nums) if operations[c] == "+" else prod(nums)
            nums = []
        num = ''
    return res

print(calc(numbers, operations))
