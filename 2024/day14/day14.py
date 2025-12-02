import re
from time import sleep

def read_input():
    HEIGHT = 103
    WIDTH = 101
    robots = []
    with open('day14-input.txt', 'r') as f:
        robot_pattern = r'^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$'
        for line in f:
            r_match = re.match(robot_pattern, line.strip())
            pos_vel = list(map(int, r_match.groups()))
            robots.append((pos_vel[:2], pos_vel[2:]))
    return HEIGHT, WIDTH, robots

def part1(puzzle_input):
    height, width, robots = puzzle_input
    
    quadrants_limts = [
        ((0, 0), (height // 2, width // 2)),                      # Q1
        ((0, (width + 1) // 2), (height // 2, width)),            # Q2
        (((height + 1) // 2, 0), (height, width // 2)),           # Q3
        (((height + 1) // 2, (width + 1) // 2), (height, width))  # Q4
    ]
    quadrants = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4
    
    seconds = 100
    for (c, r), (dc, dr) in robots:
        newr = (r + seconds * dr) % height
        newc = (c + seconds * dc) % width
        
        for i, ((qr1, qc1), (qr2, qc2)) in enumerate(quadrants_limts):
            if qr1 <= newr < qr2 and qc1 <= newc < qc2:
                quadrants[i] += 1
    
    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    print(safety_factor)
    
def part2(puzzle_input):
    height, width, robots = puzzle_input
    
    def move(seconds):
        adds = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        grid = [[' '] * width for _ in range(height)]
        adjacent = 0
        for (c, r), (dc, dr) in robots:
            newr = (r + seconds * dr) % height
            newc = (c + seconds * dc) % width
            grid[newr][newc] = '#'
            for radd, cadd in adds:
                rr, cc = newr + radd, newc + cadd
                if 0 <= rr < height and 0 <= cc < width and grid[rr][cc] == '#':
                    adjacent += 1
        return grid, adjacent
    
    seconds = 0
    last_displayed_second = 0
    erase = 0
    try:
        while True:
            grid, adjacent = move(seconds)
            
            if adjacent > 250:
                last_displayed_second = seconds
                
                print(f'Time Passed: {seconds} seconds')
                for row in grid:
                    print(''.join(row))
                
                sleep(0.5)
                
                # Reset terminal output
                # height := erase grid output
                # +1     := erase "Time Passed: \d+ seconds" line
                erase = 0
                for _ in range(height + 1):
                    print('\033[A\033[A')
                    erase += 1
                
                sleep(0.1)
            
            seconds += 1
    except KeyboardInterrupt:
        # Finish erasing any unerased lines
        # +1 := erase KeyboardInterrupt output
        for erase in range(erase, height + 2):
            print('\033[A\033[A')
            
        grid, _ = move(last_displayed_second)
        print(f'\nChristmas: {last_displayed_second} seconds')
        for row in grid:
            print(''.join(row))

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
