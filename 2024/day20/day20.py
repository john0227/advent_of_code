def read_input():
    maze = []
    with open('day20-input.txt', 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

def dfs(maze, start):
    R, C = len(maze), len(maze[0])
    adds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    r, c = start
    dists = [[float('inf')] * C for _ in range(R)]
    dists[r][c] = 0
    d = 1
    while maze[r][c] != 'E':
        for dr, dc in adds:
            newr, newc = r + dr, c + dc
            if 0 <= newr < R and 0 <= newc < C and maze[newr][newc] != '#' and dists[newr][newc] > d:
                r, c = newr, newc
                dists[r][c] = d
                break
        d += 1
    return dists

def count_best_cheats_from_point(maze, start, max_cheat_time, min_time_save, dists):
    R, C = len(maze), len(maze[0])
    sr, sc = start
    counts = 0
    for r in range(max(0, sr - max_cheat_time), min(R, sr + max_cheat_time + 1)):
        for c in range(max(0, sc - max_cheat_time), min(C, sc + max_cheat_time + 1)):
            no_cheat_dist = dists[r][c] - dists[sr][sc]
            cheat_dist = abs(r - sr) + abs(c - sc)  # Manhattan Distance
            if cheat_dist <= max_cheat_time and maze[r][c] != '#' and no_cheat_dist - cheat_dist >= min_time_save:
                counts += 1
    return counts

def count_best_cheats(maze, start, max_cheat_time, min_time_save):
    # Get vanilla dists matrix (no cheats)
    dists = dfs(maze, start)
    
    cheats = 0
    for r, row in enumerate(dists):
        for c, dist in enumerate(row):
            if dist == float('inf'):
                continue
            
            # For each cell in path to end, count number of cells reachable by cheating (optimally)
            cheats += count_best_cheats_from_point(maze, (r, c), max_cheat_time, min_time_save, dists)
    return cheats

def part1(puzzle_input):
    maze = puzzle_input
    
    start = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
                break
        if start: break
    
    MAX_CHEAT_TIME = 2
    MIN_TIME_SAVE = 100
    
    ans = count_best_cheats(maze, start, MAX_CHEAT_TIME, MIN_TIME_SAVE)
    print(ans)
    
def part2(puzzle_input):
    maze = puzzle_input
    
    start = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
                break
        if start: break
    
    MAX_CHEAT_TIME = 20
    MIN_TIME_SAVE = 100
    
    ans = count_best_cheats(maze, start, MAX_CHEAT_TIME, MIN_TIME_SAVE)
    print(ans)


if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
