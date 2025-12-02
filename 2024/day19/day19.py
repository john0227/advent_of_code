from collections import defaultdict

def read_input():
    towels = None
    designs = []
    with open('day19-input.txt', 'r') as f:
        towels = f.readline().strip().split(', ')
        f.readline()  # read empty line
        
        for line in f:
            designs.append(line.strip())
    return towels, designs

def part1(puzzle_input):
    towels, designs = puzzle_input
    
    lookup = defaultdict(list)
    for towel in towels:
        lookup[towel[0]].append(towel)
    
    possible = 0
    for design in designs:
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if not dp[i]: continue
            for towel in lookup[design[i]]:
                if design[i:i + len(towel)] == towel:
                    dp[i + len(towel)] = True
        possible += dp[-1]
    print(possible)

def part2(puzzle_input):
    towels, designs = puzzle_input
    
    lookup = defaultdict(list)
    for towel in towels:
        lookup[towel[0]].append(towel)
    
    possible = 0
    for design in designs:
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            if not dp[i]: continue
            for towel in lookup[design[i]]:
                if design[i:i + len(towel)] == towel:
                    dp[i + len(towel)] += dp[i]
        possible += dp[-1]
    print(possible)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
