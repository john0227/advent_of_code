class HaltException(Exception):
    pass

def read_input():
    with open('day17-input.txt', 'r') as f:
        A = int(f.readline().strip()[12:])
        B = int(f.readline().strip()[12:])
        C = int(f.readline().strip()[12:])
        program = list(map(int, f.read().strip()[9:].split(',')))
    return A, B, C, program

"""
Explanation of program (see day17-input.txt):

Step 1: (2, 4) -> B = A & 7
Step 2: (1, 5) -> B = B ^ 0b101  (toggle third to last and last bits)
Step 3: (7, 5) -> C = A >> B
Step 4: (0, 3) -> A = A >> 3
Step 5: (4, 0) -> B = B ^ C
Step 6: (1, 6) -> B = B ^ 0b110  (toggle third to last and second to last bits)
Step 7: (5, 5) -> print (B & 7)
Step 8: (3, 0) -> jump to 0 (if A != 0)

Overall, we can see that:
  - only the last 3 bits of B matters
  - via Steps 7 and 8, the program will print and jump (bits(A) // 3) number of times
    - where bits(A) := number of bits in A
  - via Step 3, A will be shifted 0-7 bits to the right
  - via Step 5, last 3 bits of C matters (as B ^ C and only last 3 bits of B matters)
    - via Steps 3 and 5, C will depend on last 0-10 bits of A
"""

class Computer:
    def __init__(self, A, B, C):
        self.registers = [A, B, C]
        self.iptr = 0
        self.commands = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
    
    def eval_combo_operand(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 7:
            raise HaltException()
        return self.registers[operand - 4]
    
    def adv(self, operand):
        num = self.registers[0]
        rshift = self.eval_combo_operand(operand)
        self.registers[0] = num >> rshift
    
    def bxl(self, operand):
        self.registers[1] ^= operand
    
    def bst(self, operand):
        self.registers[1] = self.eval_combo_operand(operand) & 7
    
    def jnz(self, operand):
        self.iptr = operand if self.registers[0] != 0 else self.iptr + 2
    
    def bxc(self, operand):
        self.registers[1] ^= self.registers[2]
    
    def out(self, operand):
        return self.eval_combo_operand(operand) & 7
    
    def bdv(self, operand):
        num = self.registers[0]
        rshift = self.eval_combo_operand(operand)
        self.registers[1] = num >> rshift
    
    def cdv(self, operand):
        num = self.registers[0]
        rshift = self.eval_combo_operand(operand)
        self.registers[2] = num >> rshift
    
    def run(self, program, part2=False):
        self.iptr = 0
        outs = []
        while self.iptr < len(program):
            cmd = program[self.iptr]
            operand = program[self.iptr + 1]
            
            res = self.commands[cmd](operand)
            if cmd == 5:
                outs.append(res)
                if part2 and (len(outs) > len(program) or res != program[len(outs) - 1]):
                    return outs
            
            if cmd != 3:
                self.iptr += 2
        return outs

def part1(puzzle_input):
    A, B, C, program = puzzle_input
    
    computer = Computer(A, B, C)
    res = computer.run(program)
    print(','.join(map(str, res)))

def part2(puzzle_input):
    _, B, C, program = puzzle_input
    
    # Start with all combinations of 10 bit integers that produce the first value of program
    valid = []
    for a in range(0, 2048):
        computer = Computer(a, B, C)
        outs = computer.run(program, part2=True)
        if outs and outs[0] == program[0]:
            valid.append(a)
    
    # Iteratively add three bits to the front of previously valid inputs
    # as three bits add one more output by the program
    bits = 10
    matched = []
    for i in range(1, 16):
        newvalid = []
        tested = set()
        for v in valid:
            for prefix in range(8):
                A = (prefix << bits) | v
                
                if A in tested:
                    continue
                tested.add(A)
                
                computer = Computer(A, B, C)
                outs = computer.run(program, part2=True)
                
                if outs == program:
                    matched.append(A)
                
                if len(outs) > i and outs[i] == program[i]:
                    newvalid.append(A)
        if matched:
            break
        
        valid = newvalid
        bits += 3
    
    print(min(matched))

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
