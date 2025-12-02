import heapq

def read_input():
    maze = []
    with open('day16-input.txt', 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

def part1(puzzle_input):
    maze = puzzle_input
    
    R, C = len(maze), len(maze[0])
    start, end = None, None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pq = [(0, 1, start), (1000, 0, start), (1000, 3, start)]
    D = [[[float('inf')] * 4 for _ in range(C)] for _ in range(R)]
    D[start[0]][start[1]][1] = 0
    D[start[0]][start[1]][0] = 1000
    D[start[0]][start[1]][3] = 1000
    while pq:
        score, d, (r, c) = heapq.heappop(pq)
        if (r, c) == end:
            print(score)
            break
        
        if D[r][c][d] < score:
            continue
        D[r][c][d] = score
        
        # Option 1: Continue one step in current direction
        newr, newc = r + dirs[d][0], c + dirs[d][1]
        if 0 <= newr < len(maze) and 0 <= newc < len(maze[0]) and maze[newr][newc] != '#' and D[newr][newc][d] > score + 1:
            heapq.heappush(pq, (score + 1, d, (newr, newc)))
        
        # Option 2: Rotate 90 degrees clockwise (only do rotating if there is empty space in front)
        newd = (d + 1) % 4
        newr, newc = r + dirs[newd][0], c + dirs[newd][1]
        if 0 <= newr < len(maze) and 0 <= newc < len(maze[0]) and maze[newr][newc] != '#' and D[newr][newc][newd] > score + 1001:
            heapq.heappush(pq, (score + 1001, newd, (newr, newc)))
        
        # Option 3: Rotate 90 degrees counter-clockwise (only do rotating if there is empty space in front)
        newd = (d - 1) % 4
        newr, newc = r + dirs[newd][0], c + dirs[newd][1]
        if 0 <= newr < len(maze) and 0 <= newc < len(maze[0]) and maze[newr][newc] != '#' and D[newr][newc][newd] > score + 1001:
            heapq.heappush(pq, (score + 1001, newd, (newr, newc)))

def part2(puzzle_input):
    maze = puzzle_input
    
    R, C = len(maze), len(maze[0])
    start, end = None, None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pq = [(0, 1, start, set()), (1000, 0, start, set()), (1000, 3, start, set())]
    D = [[[float('inf')] * 4 for _ in range(C)] for _ in range(R)]
    D[start[0]][start[1]][1] = 0
    D[start[0]][start[1]][0] = 1000
    D[start[0]][start[1]][3] = 1000
    bestpaths = {start, end}
    bestscore = float('inf')
    while pq:
        score, d, (r, c), path = heapq.heappop(pq)
        if score > bestscore:
            break
        
        if (r, c) == end:
            bestscore = score
            bestpaths |= path
            continue
        
        if D[r][c][d] < score:
            continue
        D[r][c][d] = score
        path = path | {(r, c)}
        
        newpath = set(path)
        # Option 1: Continue one step in current direction
        newr, newc = r + dirs[d][0], c + dirs[d][1]
        if 0 <= newr < len(maze) and 0 <= newc < len(maze[0]) and maze[newr][newc] != '#' and D[newr][newc][d] > score + 1:
            heapq.heappush(pq, (score + 1, d, (newr, newc), newpath))
        
        # Option 2: Rotate 90 degrees clockwise (only do rotating if there is empty space in front)
        newd = (d + 1) % 4
        newr, newc = r + dirs[newd][0], c + dirs[newd][1]
        if 0 <= newr < len(maze) and 0 <= newc < len(maze[0]) and maze[newr][newc] != '#' and D[newr][newc][newd] > score + 1001:
            heapq.heappush(pq, (score + 1001, newd, (newr, newc), newpath))
        
        # Option 3: Rotate 90 degrees counter-clockwise (only do rotating if there is empty space in front)
        newd = (d - 1) % 4
        newr, newc = r + dirs[newd][0], c + dirs[newd][1]
        if 0 <= newr < len(maze) and 0 <= newc < len(maze[0]) and maze[newr][newc] != '#' and D[newr][newc][newd] > score + 1001:
            heapq.heappush(pq, (score + 1001, newd, (newr, newc), newpath))
    
    print(len(bestpaths))

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
