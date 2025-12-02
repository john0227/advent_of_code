#!/bin/bash

DAY=$1

if [[ -z $DAY ]]; then
    echo -e "Please provide which day to test\n" >&2
    echo "Example:" >&2
    echo "  ./test.sh <day>" >&2
    exit 1
fi

re='^[0-9]+$'
if ! [[ $DAY =~ $re ]] ; then
   echo "day should be a number" >&2
   exit 1
fi

(
    cwd=$(dirname $(realpath $0))
    testdir="$cwd/day${DAY}"

    if [[ ! -d $testdir ]]; then
        echo "You have not started day ${DAY} yet!!" >&2
        exit 1
    fi

    cd $testdir
    python3 "day${DAY}.py"
)
