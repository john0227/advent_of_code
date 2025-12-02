from collections import defaultdict

def read_input():
    with open('day5-input.txt', 'r') as f:
        rules = set()
        for line in f:
            line = line.strip()
            if line == '': break
            rules.add(tuple(map(int, line.split('|'))))
        
        updates = []
        for line in f:
            updates.append(list(map(int, line.strip().split(','))))
    return rules, updates

def part1(puzzle_input):
    rules, updates = puzzle_input
    
    ans = 0
    for update in updates:
        n = len(update)
        invalid = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (update[j], update[i]) in rules:
                    invalid = True
                    break
            if invalid: break
        if invalid: continue
        ans += update[n // 2]
    
    print(ans)

def part2(puzzle_input):
    rules, updates = puzzle_input
    
    ans = 0
    for update in updates:
        n = len(update)
        valid = True
        ranks = defaultdict(int)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (update[j], update[i]) in rules:
                    ranks[update[j]] += 1
                    valid = False
                else:
                    ranks[update[i]] += 1
        if valid: continue
        for page, rank in ranks.items():
            if rank == n // 2:
                ans += page
    
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
