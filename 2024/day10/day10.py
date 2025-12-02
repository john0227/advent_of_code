def read_input():
    grid = []
    with open('day10-input.txt', 'r') as f:
        for line in f:
            grid.append(list(map(int, line.strip())))
    return grid

def part1(puzzle_input):
    grid = puzzle_input
    
    R, C = len(grid), len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def dfs(r, c, visited):
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        
        height = grid[r][c]
        if height == 9:
            return 1
        
        score = 0
        for dr, dc in dirs:
            newr, newc = r + dr, c + dc
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == height + 1:
                score += dfs(newr, newc, visited)
        return score
    
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                ans += dfs(r, c, set())
    print(ans)

def part2(puzzle_input):
    grid = puzzle_input
    
    R, C = len(grid), len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def dfs(r, c):
        height = grid[r][c]
        if height == 9:
            return 1
        
        score = 0
        for dr, dc in dirs:
            newr, newc = r + dr, c + dc
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == height + 1:
                score += dfs(newr, newc)
        return score
    
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                ans += dfs(r, c)
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
