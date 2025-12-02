import sys

fp = sys.argv[1]

with open(fp, 'r') as f:
    input = f.readlines()

dial = 50
pw = 0
for line in input:
    line = line.strip()

    direction = line[0]
    number = int(line[1:])

    if direction == 'R':
        dial += number
    else:
        # get negative mod of dial
        dial = (dial if dial == 0 else dial - 100) - number

    rot = abs(dial) // 100
    dial %= 100
    pw += rot

print(pw)

# dial = 50
# pw = 0
# for line in input:
#     line = line.strip()
#     direction = -1 if line[0] == 'L' else 1
#     number = int(line[1:])
#
#     for _ in range(number):
#         dial = (dial + direction) % 100
#         if dial == 0:
#             pw += 1
#
# print(pw)
