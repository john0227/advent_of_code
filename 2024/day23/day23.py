from collections import defaultdict


def read_input():
    graph = defaultdict(set)
    with open('day23-input.txt', 'r') as f:
        for line in f:
            com1, com2 = line.strip().split('-')
            graph[com1].add(com2)
            graph[com2].add(com1)
    return graph

def _find_connected(graph, curr, group, seen):
    for adj in graph[curr]:
        if adj in group:
            continue
        
        connected = all(adj in graph[com] for com in group)
        if not connected:
            continue
        
        group.add(adj)
        key = tuple(sorted(group))
        if key not in seen:
            seen.add(key)
            _find_connected(graph, adj, group, seen)
        group.discard(adj)

def find_connected(graph, curr, seen=None, size=-1):
    connected = seen or set()
    _find_connected(graph, curr, {curr}, connected)
    
    if size == -1:
        size = max(len(group) for group in connected)
    return {group for group in connected if len(group) == size}
        
def part1(puzzle_input):
    graph = puzzle_input
    
    seen, sets_of_3 = set(), set()
    for com in graph:
        if com[0] != 't': continue
        sets_of_3 |= find_connected(graph, com, seen, 3)
    print(len(sets_of_3))

def part2(puzzle_input):
    graph = puzzle_input
    
    max_connected, maxsize = None, -1
    seen = set()
    for com in graph:
        for connected in find_connected(graph, com, seen=seen):
            if len(connected) > maxsize:
                maxsize = len(connected)
                max_connected = connected
    
    print(','.join(max_connected))

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
