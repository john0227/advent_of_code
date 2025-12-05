import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    intervals = []
    # Read ranges until empty line
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        start, end = line.split("-")
        intervals.append([int(start), int(end)])
    # Read ingredient IDs until EOF
    ingredient_ids = list(map(int, file.read().split()))

def merge_intervals(intervals) -> list[list[int]]:
    intervals.sort(key=lambda i: (i[0], -i[1]))
    merged = [intervals[0]]
    for intvl in intervals:
        start1, end1 = intvl
        start2, end2 = merged[-1]
        if start2 <= start1 and end1 <= end2:
            continue
        if start1 <= end2:
            merged[-1][1] = end1
        else:
            merged.append(intvl)
    return merged

def is_fresh(intervals, ingredient_id) -> bool:
    low, high = 0, len(intervals) - 1
    while low <= high:
        mid = (low + high) // 2
        start, end = intervals[mid]
        if start <= ingredient_id <= end:
            return True
        if ingredient_id < start:
            high = mid - 1
        else:
            low = mid + 1
    return False

intervals = merge_intervals(intervals)

part1 = 0
for iid in ingredient_ids:
    part1 += int(is_fresh(intervals, iid))
print(part1)

part2 = 0
for start, end in intervals:
    part2 += end - start + 1
print(part2)
