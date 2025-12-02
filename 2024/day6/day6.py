def read_input():
    grid = []
    start = None
    with open('day6-input.txt', 'r') as f:
        r = 0
        for line in f:
            line = line.strip()
            grid.append(list(line))
            if '^' in line:
                start = (r, line.index('^'))
            r += 1
    return grid, start

visited = set()

def part1(puzzle_input):
    grid, start = puzzle_input
    
    R, C = len(grid), len(grid[0])
    r, c = start
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    ans = 0
    while True:
        if grid[r][c] != 'X':
            ans += 1
            grid[r][c] = 'X'
        visited.add((r, c))
        
        newr, newc = r + dirs[d][0], c + dirs[d][1]
        if not (0 <= newr < R and 0 <= newc < C):
            break
        
        while grid[newr][newc] == '#':
            d = (d + 1) % 4
            newr, newc = r + dirs[d][0], c + dirs[d][1]
        r, c = newr, newc
    print(ans)

def part2(puzzle_input):
    grid, start = puzzle_input
    
    R, C = len(grid), len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = 0
    for rr in range(R):
        for cc in range(C):
            if grid[rr][cc] == '#' or (rr, cc) not in visited or (rr, cc) == start:
                continue
            
            grid[rr][cc] = '#'
            
            d = 0
            r, c = start
            seen = set()  # (r, c, d)
            
            while True:
                newr, newc = r + dirs[d][0], c + dirs[d][1]
                if not (0 <= newr < R and 0 <= newc < C):
                    break
                
                # See https://www.reddit.com/r/adventofcode/comments/1h7tovg/comment/m0p4uvm/
                while grid[newr][newc] == '#':
                    d = (d + 1) % 4
                    newr, newc = r + dirs[d][0], c + dirs[d][1]
                    
                r, c = newr, newc
                if (r, c, d) in seen:
                    ans += 1
                    break
                seen.add((r, c, d))
            
            grid[rr][cc] = '.'
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
