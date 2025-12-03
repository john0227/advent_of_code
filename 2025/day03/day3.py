from itertools import pairwise
import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().split()

def max_joltage(bank: str) -> int:
    max1, max2 = -1, -1
    for bat1, bat2 in pairwise(bank):
        bat1, bat2 = int(bat1), int(bat2)
        if max1 == -1 or max1 < bat1:
            max1 = bat1
            max2 = bat2
        elif max2 < bat2:
            max2 = bat2
    return max1 * 10 + max2

ans = 0
for bank in lines:
    ans += max_joltage(bank)
print(ans)
