def read_input():
    with open('day9-input.txt', 'r') as f:
        dm_str = f.read().strip()
        diskmap = []
        for i, c in enumerate(dm_str):
            diskmap.extend([(i >> 1) if i & 1 == 0 else None] * int(c))
    return dm_str, diskmap

def part1(puzzle_input):
    _, diskmap = puzzle_input
    
    left, right = 0, len(diskmap) - 1
    while left < right:
        while left < len(diskmap) and diskmap[left] is not None: left += 1
        while right >= 0 and diskmap[right] is None: right -= 1
        if left < right:
            diskmap[left], diskmap[right] = diskmap[right], diskmap[left]
        left += 1
        right -= 1
    
    checksum = 0
    for i, file in enumerate(diskmap):
        if file is None: break
        checksum += i * file
    print(checksum)

def part2(puzzle_input):
    dm_str, _ = puzzle_input
    
    comb = filemap, freemap = [], []
    loc = 0
    for i, file in enumerate(dm_str):
        comb[i & 1].append([loc, int(file)])
        loc += int(file)
    
    for file in reversed(filemap):
        i, filesize = file
        for free in freemap:
            j, freesize = free
            if i > j and freesize >= filesize:
                file[0] = j
                free[0] += filesize
                free[1] -= filesize
                break
            if i < j:
                break
    
    checksum = 0
    for fid, (i, filesize) in enumerate(filemap):
        checksum += fid * (((i + i + filesize - 1) * filesize) // 2)
    print(checksum)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
