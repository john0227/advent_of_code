import sys


fp = sys.argv[1]
with open(fp, "r") as f:
    input = f.read().split(",")

def get_invalid_ids(start: int, end: int) -> list[int]:
    ans = []
    for num in range(start, end + 1):
        snum = str(num)
        n = len(snum)
        for div in range(2, n + 1):
            if n % div != 0:
                continue

            prev = snum[:n // div]
            valid = True
            for i in range(1, div):
                curr = snum[i * (n // div):(i + 1) * (n // div)]
                if prev != curr:
                    valid = False
                    break
            if valid:
                ans.append(num)
                break
    return ans

invalid_ids = []
for rng in input:
    start, end = list(map(int, rng.split('-')))
    invalid_ids.extend(get_invalid_ids(start, end))
print(sum(invalid_ids))
