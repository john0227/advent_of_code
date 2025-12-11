from collections import defaultdict
import sys


fp = sys.argv[1]
with open(fp, "r") as file:
    lines = file.read().strip().split("\n")

def make_graph(lines: list[str]) -> dict[str, list[str]]:
    graph = defaultdict(list)
    for line in lines:
        src, dests = line.split(": ")
        graph[src].extend(dests.split())
    return graph

def count_paths(graph, start: str = "you", end: str = "out", nodes_to_visit: set[str] | None =None) -> int:
    def dfs(curr: str, to_visit: set[str]) -> int:
        nonlocal memo

        memokey = (curr, tuple(sorted(to_visit)))
        if memokey in memo:
            return memo[memokey]

        if curr == end:
            return int(len(to_visit) == 0)

        res = 0
        for adj in graph[curr]:
            to_visit.discard(adj)
            res += dfs(adj, to_visit)
            if adj in nodes_to_visit:
                to_visit.add(adj)

        memo[memokey] = res
        return res

    memo = {}
    to_visit = set(nodes_to_visit or set())
    return dfs(start, to_visit)

graph = make_graph(lines)
ans = count_paths(graph, start="svr", nodes_to_visit={"dac", "fft"})
print(ans)
