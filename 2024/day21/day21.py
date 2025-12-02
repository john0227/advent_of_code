from functools import cache
from itertools import pairwise


def read_input():
    with open('day21-input.txt', 'r') as f:
        codes = f.read().splitlines()
    return codes

class Keypad:
    numeric_keypad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        ' ': (3, 0), '0': (3, 1), 'A': (3, 2)
    }
    directional_keypad = {
        ' ': (0, 0), '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2)
    }
    
    @classmethod
    def to_coords(cls, start, end, is_directional_keypad):
        keypad = cls.directional_keypad if is_directional_keypad else cls.numeric_keypad
        return keypad[start], keypad[end], keypad[' ']

def get_paths(start, end, invalid):
    if start == end:
        return ['A']
    
    sr, sc = start
    er, ec = end
    ir, ic = invalid
    
    ver_dist = abs(sr - er)
    hor_dist = abs(sc - ec)
    
    ver_arrow = ('v' if sr < er else '^') * ver_dist
    hor_arrow = ('>' if sc < ec else '<') * hor_dist
    
    if ver_dist == 0:
        return [hor_arrow + 'A']
    if hor_dist == 0:
        return [ver_arrow + 'A']
    if sc == ic and er == ir:
        return [hor_arrow + ver_arrow + 'A']
    if sr == ir and ec == ic:
        return [ver_arrow + hor_arrow + 'A']
    return [
        ver_arrow + hor_arrow + 'A',
        hor_arrow + ver_arrow + 'A'
    ]

@cache
def get_shortest_path(start, end, num_robots, is_directional_keypad):
    """
    - One directional keypad that you are using
    - `num_robots` directional keypads that robots are using
    - One numeric keypad (on a door) that a robot is using
    """
    start, end, invalid = Keypad.to_coords(start, end, is_directional_keypad)
    paths = get_paths(start, end, invalid)
    
    if num_robots == 0:
        return min(len(path) for path in paths)
    
    mindist = float('inf')
    for path in paths:
        dist = 0
        for s, e in pairwise('A' + path):
            dist += get_shortest_path(s, e, num_robots - 1, True)
        mindist = min(mindist, dist)
    return mindist

def part1(puzzle_input):
    codes = puzzle_input
    
    NUM_ROBOTS = 2
    
    ans = 0
    for code in codes:
        shortest_path = 0
        for start, end in pairwise('A' + code):
            shortest_path += get_shortest_path(start, end, NUM_ROBOTS, False)
        ans += int(code[:-1]) * shortest_path
    print(ans)

def part2(puzzle_input):
    codes = puzzle_input
    
    NUM_ROBOTS = 25
    
    ans = 0
    for code in codes:
        shortest_path = 0
        for start, end in pairwise('A' + code):
            shortest_path += get_shortest_path(start, end, NUM_ROBOTS, False)
        ans += int(code[:-1]) * shortest_path
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
