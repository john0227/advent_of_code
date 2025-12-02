#!/bin/bash

DAY=$1

if [[ -z $DAY ]]; then
    echo -e "error: Please provide which day to create\n" >&2
    echo "Example:" >&2
    echo "  ./create.sh <day>" >&2
    exit 1
fi

re='^[0-9]+$'
if ! [[ $DAY =~ $re ]] ; then
   echo "day should be a number" >&2
   exit 1
fi

skeleton="def read_input():
    with open('day${DAY}-input.txt', 'r') as f:
        lines = f.readlines()
    pass

def part1(puzzle_input):
    pass

def part2(puzzle_input):
    pass

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)"

(
    cwd=$(dirname $(realpath $0))
    cd "$cwd"

    newdir="${cwd}/day${DAY}"
    if [[ -d $newdir ]]; then
        echo "Day ${DAY} already exists" >&2
        exit 1
    fi

    mkdir $newdir
    touch "${newdir}/day${DAY}-input.txt"
    echo "$skeleton" > "${newdir}/day${DAY}.py"
)
