from collections import Counter, defaultdict

def read_input():
    stones = []
    with open('day11-input.txt', 'r') as f:
        stones = list(map(int, f.readline().strip().split()))
    return stones

def part1(puzzle_input):
    stones = puzzle_input
    blinks = 25
    
    for _ in range(blinks):
        newstones = []
        for stone in stones:
            if stone == 0:
                newstones.append(1)
            elif (digits := len(str(stone))) % 2 == 0:
                mask = 10 ** (digits // 2)
                newstones.append(stone // mask)
                newstones.append(stone % mask)
            else:
                newstones.append(stone * 2024)
        stones = newstones
    
    print(len(stones))

def part2(puzzle_input):
    stones = puzzle_input
    blinks = 75
    
    stones = Counter(stones)
    for _ in range(blinks):
        newstones = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                newstones[1] += count
            elif (digits := len(str(stone))) % 2 == 0:
                mask = 10 ** (digits // 2)
                newstones[stone // mask] += count
                newstones[stone % mask] += count
            else:
                newstones[stone * 2024] += count
        stones = newstones
    
    num_stones = sum(stones.values())
    print(num_stones)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
