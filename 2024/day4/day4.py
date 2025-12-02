def read_input():
    with open('day4-input.txt', 'r') as f:
        lines = f.read().split('\n')
        
    crossword = []
    for line in lines:
        crossword.append(list(line))
    return crossword

def part1(puzzle_input):
    crossword = puzzle_input
    
    R, C = len(crossword), len(crossword[0])
    
    add = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    word = 'XMAS'
    count = 0
    for r in range(R):
        for c in range(C):
            for x, y in add:
                for i in range(4):
                    if not (0 <= r + x * i < R and 0 <= c + y * i < C) or crossword[r + x * i][c + y * i] != word[i]:
                        break
                else:
                    count += 1
    print(count)

def part2(puzzle_input):
    crossword = puzzle_input
    
    R, C = len(crossword), len(crossword[0])
    
    count = 0
    for r in range(R - 2):
        for c in range(C - 2):
            back = (crossword[r][c] == 'M' and crossword[r + 1][c + 1] == 'A' and crossword[r + 2][c + 2] == 'S') or \
                   (crossword[r][c] == 'S' and crossword[r + 1][c + 1] == 'A' and crossword[r + 2][c + 2] == 'M')
            front = (crossword[r][c + 2] == 'M' and crossword[r + 1][c + 1] == 'A' and crossword[r + 2][c] == 'S') or \
                    (crossword[r][c + 2] == 'S' and crossword[r + 1][c + 1] == 'A' and crossword[r + 2][c] == 'M')
            count += (back and front)
    print(count)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
