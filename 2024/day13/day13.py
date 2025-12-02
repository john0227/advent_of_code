from math import floor
import re

def read_input():
    button_pattern = r'X\+(\d+), Y\+(\d+)$'
    prize_pattern = r'X=(\d+), Y=(\d+)$'
    games = []
    with open('day13-input.txt', 'r') as f:
        while True:
            A = list(map(int, re.search(button_pattern, f.readline().strip()).groups()))
            B = list(map(int, re.search(button_pattern, f.readline().strip()).groups()))
            prize = list(map(int, re.search(prize_pattern, f.readline().strip()).groups()))
            games.append((A, B, prize))
            
            end = f.readline()
            if not end:
                break
    return games

def part1(puzzle_input):
    games = puzzle_input
    
    tokens = 0
    for A, B, prize in games:
        AX, AY = A
        BX, BY = B
        PX, PY = prize
        mintokens = float('inf')
        for a in range(101):
            for b in range(101):
                if (a * AX + b * BX == PX) and (a * AY + b * BY == PY):
                    mintokens = min(mintokens, 3 * a + b)
        tokens += mintokens if mintokens != float('inf') else 0
    print(tokens)

def part2(puzzle_input):
    games = puzzle_input
    
    def is_int(num):
        return floor(num) == num
    
    tokens = 0
    for A, B, prize in games:
        AX, AY = A
        BX, BY = B
        PX, PY = prize
        
        # Offset prize coordinates
        PX += 10000000000000
        PY += 10000000000000
        
        """
        Solve for x = [a b], in Ax = B
        where,
            A = [[AX, BX],
                [AY, BY]]
            x = [a b]^T
            B = [PX, PY]^T
        
        i.e.,
        [AX BX][a] = [PX]
        [AY BY][b] = [PY]
        
        Note, inverse of A is the following:
            |A| * A^-1 = [[ BY, -BX],
                          [-AY,  AX]]
        """
        det = AX * BY - AY * BX
        if det != 0:
            a = (PX * BY - PY * BX) / det
            b = (PY * AX - PX * AY) / det
            if is_int(a) and is_int(b):
                tokens += 3 * int(a) + int(b)
    print(tokens)

if __name__ == '__main__':
    puzzle_input = read_input()
    # part1(puzzle_input)
    part2(puzzle_input)
