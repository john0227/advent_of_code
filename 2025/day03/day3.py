import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().split()

def max_joltage(bank: str, n=12) -> int:
    m = len(bank)
    left = 0
    res = 0
    for right in range(m - n, m):
        max_idx, max_bat = -1, -1
        for j in range(left, right + 1):
            bat = int(bank[j])
            if max_bat < bat:
                max_idx = j
                max_bat = bat
        res = res * 10 + max_bat
        left = max_idx + 1
    return res

ans = 0
for bank in lines:
    ans += max_joltage(bank)
print(ans)
