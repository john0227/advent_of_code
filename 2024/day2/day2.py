from itertools import pairwise

def read_input():
    with open('day2-input.txt', 'r') as f:
        lines = f.readlines()
    
    reports = []
    for line in lines:
        reports.append(list(map(int, line.split())))
    return reports

def part1(puzzle_input):
    reports = puzzle_input
    
    num_safe = 0
    for report in reports:
        if report[0] == report[1]:
            continue
        
        inc = report[0] < report[1]
        num_safe += all(
            ((inc and lev1 < lev2) or (not inc and lev1 > lev2)) and abs(lev1 - lev2) <= 3
            for lev1, lev2 in pairwise(report)
        )
    print(num_safe)

def part2(puzzle_input):
    reports = puzzle_input
    
    safelines = []
    
    num_safe = 0
    for li, report in enumerate(reports):
        for i in range(len(report)):
            r = report[:i] + report[i + 1:]
            inc = r[0] < r[1]
            safe = all(
                ((inc and lev1 < lev2) or (not inc and lev1 > lev2)) and abs(lev1 - lev2) <= 3
                for lev1, lev2 in pairwise(r)
            )
            if safe:
                safelines.append(str(li))
                num_safe += 1
                break
    print(num_safe)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
