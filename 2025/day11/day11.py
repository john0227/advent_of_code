from collections import defaultdict
from functools import cache
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

def count_paths(graph, start: str = "you", end: str = "out") -> int:
    @cache
    def dfs(curr: str) -> int:
        if curr == end:
            return 1
        res = 0
        for adj in graph[curr]:
            res += dfs(adj)
        return res
    return dfs(start)

graph = make_graph(lines)
ans = count_paths(graph)
print(ans)
