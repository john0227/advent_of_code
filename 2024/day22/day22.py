from collections import defaultdict, deque
from itertools import pairwise


def read_input():
    with open('day22-input.txt', 'r') as f:
        nums = list(map(int, f.read().splitlines()))
    return nums

class RNG:
    def __init__(self, seed):
        self.secret = seed

    def mix(self, value):
        self.secret = self.secret ^ value
    
    def prune(self):
        # modulo 16777216
        # 16777216 = 2 ** 24
        self.secret &= (1 << 24) - 1
    
    def update(self, value):
        self.mix(value)
        self.prune()

    def generate(self):
        while True:
            self.update(self.secret << 6)
            self.update(self.secret >> 5)
            self.update(self.secret << 11)
            yield self.secret

def part1(puzzle_input):
    nums = puzzle_input
    
    ITERATIONS = 2000
    
    ans = 0
    for num in nums:
        rng = RNG(num)
        for i, secret in enumerate(rng.generate()):
            if i == ITERATIONS - 1:
                ans += secret
                break
    print(ans)

def part2(puzzle_input):
    nums = puzzle_input
    
    ITERATIONS = 2000
    
    seq2prices = defaultdict(int)
    for num in nums:
        sequences = set()
        sequence = deque([])
        rng = RNG(num)
        for i, (p1, p2) in enumerate(pairwise(rng.generate()), start=1):
            p1 %= 10
            p2 %= 10
            
            sequence.append(str(p2 - p1))
            if len(sequence) == 4:
                key = ','.join(sequence)
                sequence.popleft()
                if key not in sequences:
                    seq2prices[key] += p2
                    sequences.add(key)
            
            if i == ITERATIONS - 1:
                break
    
    max_bananas = max(bananas for bananas in seq2prices.values())
    print(max_bananas)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
