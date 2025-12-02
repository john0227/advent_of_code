from collections import deque

def read_input():
    N = 71
    byte_coords = []
    with open('day18-input.txt', 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split(','))
            byte_coords.append((x, y))
    return N, byte_coords

def bfs(grid):
    N = len(grid)
    adds = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dq = deque([(0, 0)])
    visited = set()
    end = (N - 1, N - 1)
    dist = 0
    while dq:
        for _ in range(len(dq)):
            r, c = dq.popleft()
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            for radd, cadd in adds:
                newr, newc = r + radd, c + cadd
                if (newr, newc) == end:
                    return dist + 1
                if 0 <= newr < N and 0 <= newc < N and grid[newr][newc] == '.' and (newr, newc) not in visited:
                    dq.append((newr, newc))
        dist += 1
    return -1

def part1(puzzle_input):
    N, byte_coords = puzzle_input
    
    num_bytes = 1024
    grid = [['.'] * N for _ in range(N)]
    for i, (x, y) in enumerate(byte_coords):
        grid[y][x] = '#'
        if i == num_bytes - 1:
            break

    steps = bfs(grid)
    print(steps)

def part2(puzzle_input):
    N, byte_coords = puzzle_input
    
    def alter_grid(grid, start, end):
        """
        If start < end:
            Fills grid with bytes in byte_coords[start:end+1]
              i.e., including both start and end
        If start > end:
            Removes bytes from grid in byte_coords[end+1:start+1]
              i.e., including start and excluding end
        """
        if start == end:
            return
        
        replace = '#'
        if start > end:
            start, end = end + 1, start
            replace = '.'
        
        for i in range(start, end + 1):
            x, y = byte_coords[i]
            grid[y][x] = replace
    
    byte_ptr = 1024
    grid = [['.'] * N for _ in range(N)]
    alter_grid(grid, 0, byte_ptr)
    
    # Binary search to find byte that blocks off START from END
    low = 0
    high = len(byte_coords) - 1
    while low < high:
        mid = (low + high) // 2
        
        # fill/remove bytes
        alter_grid(grid, byte_ptr, mid)
        byte_ptr = mid
        
        if bfs(grid) != -1:  # Can reach end
            low = mid + 1
        else:                # Cannot reach end
            high = mid
    
    x, y = byte_coords[high]
    print(x, y, sep=',')

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
