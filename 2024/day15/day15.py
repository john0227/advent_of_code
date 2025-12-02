def read_input():
    grid = []
    moves = []
    with open('day15-input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line == '': break
            grid.append(list(line))
        for line in f:
            moves.append(line.strip())
        moves = ''.join(moves)
    return grid, moves

def part1(puzzle_input):
    def can_push(grid, r, c, dr, dc):
        # (r, c) := current coordinate of robot
        # dr, dc := direction of robot
        # (r + dr, c + dc) must be a box ('O')
        
        while True:
            r, c = r + dr, c + dc
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == '#':
                return False
            if grid[r][c] == '.':
                return True
        return False
    
    grid, moves = puzzle_input
    grid = [grid[r][:] for r in range(len(grid))]
    
    R, C = len(grid), len(grid[0])
    dirs = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    
    r, c = None, None
    for rr in range(R):
        for cc in range(C):
            if grid[rr][cc] == '@':
                r, c = rr, cc
                grid[rr][cc] = '.'
                
    
    for move in moves:
        radd, cadd = dirs[move]
        newr, newc = r + radd, c + cadd
        if not (0 <= newr < R and 0 <= newc < C) or grid[newr][newc] == '#':
            continue
        
        if grid[newr][newc] == 'O':
            if not can_push(grid, r, c, radd, cadd):
                continue
            
            boxr, boxc = newr, newc
            while grid[boxr][boxc] == 'O':
                boxr, boxc = boxr + radd, boxc + cadd
            grid[newr][newc] = '.'
            grid[boxr][boxc] = 'O'
        r, c = newr, newc

    ans = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'O':
                ans += r * 100 + c
    print(ans)

def part2(puzzle_input):
    grid, moves = puzzle_input
    
    cellmap = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.'
    }
    grid = [list(''.join(cellmap[cell] for cell in row)) for row in grid]
    
    R, C = len(grid), len(grid[0])
    
    def can_push(grid, r, c, dr, dc):
        # (r, c) := current coordinate of robot
        # dr, dc := direction of robot
        # (r + dr, c + dc) must be a box ('[' or ']')
        return can_push_hor(grid, r, c, dc) if dr == 0 else can_push_ver(grid, r, c, dr)
    
    def can_push_hor(grid, r, c, dc):
        while True:
            c += dc
            if not (0 <= c < len(grid[0])) or grid[r][c] == '#':
                return False
            if grid[r][c] == '.':
                return True
        return False
    
    def can_push_ver(grid, r, c, dr):
        left = c if grid[r + dr][c] == '[' else c - 1
        right = c if grid[r + dr][c] == ']' else c + 1
        while True:
            r += dr
            if grid[r][left] == ']': left -= 1
            if grid[r][right] == '[': right += 1
            
            newleft, newright = float('inf'), float('-inf')
            is_box = False
            for cc in range(left, right + 1):
                if not (0 <= r < R) or grid[r][cc] == '#':
                    return False
                if grid[r][cc] in '[]':
                    if grid[r][cc] == ']': newright = max(newright, cc)
                    elif grid[r][cc] == '[': newleft = min(newleft, cc)
                    is_box = True
            left, right = newleft, newright
            if not is_box:
                return True
        return False
    
    def push_boxes(grid, r, c, dr, dc):
        # (r, c) := current coordinate of robot
        # dr, dc := direction of robot        
        # (r + dr, c + dc) must be a box ('[' or ']')
        push_boxes_hor(grid, r, c, dc) if dr == 0 else push_boxes_ver(grid, r, c, dr)
        
    def push_boxes_hor(grid, r, c, dc):
        prev = grid[r][c]
        c += dc
        while grid[r][c] in '[]':
            prev, grid[r][c] = grid[r][c], prev
            c += dc
        grid[r][c] = prev
    
    def push_boxes_ver(grid, r, c, dr):
        left = c if grid[r + dr][c] == '[' else c - 1
        right = c if grid[r + dr][c] == ']' else c + 1
        prev = ('..', left, right)
        while True:
            r += dr
            if grid[r][left] == ']': left -= 1
            if grid[r][right] == '[': right += 1
            
            newleft, newright = float('inf'), float('-inf')
            is_box = False
            for cc in range(left, right + 1):
                if grid[r][cc] in '[]':
                    if grid[r][cc] == ']': newright = max(newright, cc)
                    elif grid[r][cc] == '[': newleft = min(newleft, cc)
                    is_box = True
            left, right = newleft, newright
            
            if not is_box:
                break
            
            prevbox, prevleft, prevright = prev
            prev = (grid[r][left:right + 1], left, right)
            for cc in range(min(left, prevleft), max(right, prevright) + 1):
                if cc < prevleft or cc > prevright:
                    grid[r][cc] = '.'
                else:
                    grid[r][cc] = prevbox[cc - prevleft]
        
        prevbox, prevleft, prevright = prev
        for cc in range(min(left, prevleft), max(right, prevright) + 1):
            if cc < prevleft or cc > prevright:
                grid[r][cc] = '.'
            else:
                grid[r][cc] = prevbox[cc - prevleft]
    
    dirs = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    
    r, c = None, None
    for rr in range(R):
        for cc in range(C):
            if grid[rr][cc] == '@':
                r, c = rr, cc
                grid[rr][cc] = '.'
    
    for move in moves:
        radd, cadd = dirs[move]
        newr, newc = r + radd, c + cadd
        if not (0 <= newr < R and 0 <= newc < C) or grid[newr][newc] == '#':
            continue
        
        if grid[newr][newc] in '[]':
            if not can_push(grid, r, c, radd, cadd):
                continue
            push_boxes(grid, r, c, radd, cadd)
        r, c = newr, newc

    ans = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '[':
                ans += r * 100 + c
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
