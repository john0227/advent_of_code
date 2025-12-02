from collections import defaultdict

def read_input():
    grid = []
    with open('day8-input.txt', 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def part1(puzzle_input):
    grid = puzzle_input
    R, C = len(grid), len(grid[0])
    
    antennas = defaultdict(list)
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val != '.':
                antennas[val].append((r, c))
    
    antinodes = set()
    for coords in antennas.values():
        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                r1, c1 = coords[i]
                r2, c2 = coords[j]
                dr, dc = r1 - r2, c1 - c2
                
                rr1, cc1 = r1 + dr, c1 + dc
                rr2, cc2 = r2 - dr, c2 - dc
                
                if 0 <= rr1 < R and 0 <= cc1 < C:
                    antinodes.add((rr1, cc1))
                if 0 <= rr2 < R and 0 <= cc2 < C:
                    antinodes.add((rr2, cc2))
    print(len(antinodes))

def part2(puzzle_input):
    grid = puzzle_input
    R, C = len(grid), len(grid[0])
    
    antennas = defaultdict(list)
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val != '.':
                antennas[val].append((r, c))
    
    antinodes = set()
    for coords in antennas.values():
        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                r1, c1 = coords[i]
                r2, c2 = coords[j]
                dr, dc = r1 - r2, c1 - c2
                
                while 0 <= r1 < R and 0 <= c1 < C:
                    antinodes.add((r1, c1))
                    r1, c1 = r1 + dr, c1 + dc
                while 0 <= r2 < R and 0 <= c2 < C:
                    antinodes.add((r2, c2))
                    r2, c2 = r2 - dr, c2 - dc
    print(len(antinodes))

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
