from collections import Counter, defaultdict

def read_input():
    with open('day1-input.txt', 'r') as f:
        lines = f.readlines()

    nums1, nums2 = [], []
    for line in lines:
        a, b = line.split()
        nums1.append(int(a))
        nums2.append(int(b))
    
    return nums1, nums2

def part1(puzzle_input):
    nums1, nums2 = puzzle_input
    
    nums1.sort()
    nums2.sort()
    
    print(sum(abs(a - b) for a, b in zip(nums1, nums2)))

def part2(puzzle_input):
    nums1, nums2 = puzzle_input
    
    counter = defaultdict(int, Counter(nums2))
    score = 0
    for num in nums1:
        score += num * counter[num]
    
    print(score)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
