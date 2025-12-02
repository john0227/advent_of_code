def read_input():
    equations = []
    with open('day7-input.txt', 'r') as f:
        for line in f:
            testval, nums = line.strip().split(': ')
            equations.append((int(testval), list(map(int, nums.split(' ')))))
    return equations

def part1(puzzle_input):
    equations = puzzle_input
    
    def dfs(testval, nums, i, add, cumul):
        if i == len(nums):
            return cumul == testval
        cumul = cumul + nums[i] if add else cumul * nums[i]
        return dfs(testval, nums, i + 1, add, cumul) or dfs(testval, nums, i + 1, not add, cumul)

    ans = 0
    for testval, nums in equations:
        if dfs(int(testval), nums, 0, True, 0):
            ans += testval
    print(ans)

def part2(puzzle_input):
    equations = puzzle_input
    
    ops = [
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: int(str(a) + str(b))
    ]
    def dfs(testval, nums, i, op, cumul):
        if i == len(nums):
            return cumul == testval
        cumul = ops[op](cumul, nums[i])
        return dfs(testval, nums, i + 1, 0, cumul) or \
               dfs(testval, nums, i + 1, 1, cumul) or \
               dfs(testval, nums, i + 1, 2, cumul)

    ans = 0
    for testval, nums in equations:
        if dfs(int(testval), nums, 0, 0, 0):
            ans += testval
    print(ans)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
