import re

def read_input():
    with open('day3-input.txt', 'r') as f:
        cmd = f.read()
    return cmd

def part1(puzzle_input):
    cmd = puzzle_input
    
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    cmds = re.findall(pattern, cmd)
    ans = 0
    for a, b in cmds:
        ans += int(a) * int(b)
    
    print(ans)

def part2(puzzle_input):
    cmd = puzzle_input
    
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r"(d)o\(\)|d(o)n't\(\)"
    
    matches = re.findall(rf'{mul_pattern}|{do_pattern}', cmd)
    
    ans = 0
    mul = True
    for a, b, do, dont in matches:
        if do != '':
            mul = True
        elif dont != '':
            mul = False
        elif mul:
            ans += int(a) * int(b)
    
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
