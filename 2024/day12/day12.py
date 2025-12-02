from collections import defaultdict

def read_input():
    grid = []
    with open('day12-input.txt', 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def part1(puzzle_input):
    grid = puzzle_input
    
    R, C = len(grid), len(grid[0])
    add = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def dfs(grid, r, c, groups, visited):
        if (r, c) in visited:
            return
        visited.add((r, c))
        
        curr = grid[r][c]
        for dr, dc in add:
            newr, newc = r + dr, c + dc
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == curr:
                groups[(r, c)] -= 1
                if (newr, newc) not in visited:
                    dfs(grid, newr, newc, groups, visited)
    
    price = 0
    visited = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if (r, c) not in visited:
                groups = defaultdict(lambda: 4, {(r, c): 4})
                dfs(grid, r, c, groups, visited)
                
                perimiter = sum(groups.values())
                groupsize = len(groups)
                price += perimiter * groupsize
    print(price)

class UFDS:
    def __init__(self):
        self.fence2root = {}
        self.roots = []
    
    def add_fences(self, fence_ids):
        for fence_id in fence_ids:
            if fence_id not in self.fence2root:
                rid = len(self.fence2root)
                self.fence2root[fence_id] = rid
                self.roots.append(rid)
    
    def find(self, fence_id):
        if fence_id not in self.fence2root:
            self.add_fences([fence_id])
            return root
        
        root = r = self.fence2root[fence_id]
        while root != self.roots[root]:
            root = self.roots[root]
        while self.roots[r] != root:
            r, self.roots[r] = self.roots[r], root
        return root

    def bulk_union(self, fence_ids1, fence_ids2, directions):
        """
        fence_id := (r, c, direction)
        Join pairs of fences with same direction
        """
        for fence_id1 in fence_ids1:
            if fence_id1[2] not in directions:
                continue
            for fence_id2 in fence_ids2:
                if fence_id1[2] == fence_id2[2]:
                    self.union(fence_id1, fence_id2)
    
    def union(self, fence_id1, fence_id2):
        root1 = self.find(fence_id1)
        root2 = self.find(fence_id2)
        if root1 != root2:
            self.roots[root2] = root1
    
    def get_num_fences(self):
        unique_roots = {self.find(fence_id) for fence_id in self.fence2root}
        return len(unique_roots)

def part2(puzzle_input):
    grid = puzzle_input
    
    R, C = len(grid), len(grid[0])
    add = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
    
    def get_fence_ids(r, c):
        fences = []
        for direction, (dr, dc) in enumerate(add):
            newr, newc = r + dr, c + dc
            if not (0 <= newr < R and 0 <= newc < C) or grid[newr][newc] != grid[r][c]:
                fences.append((r, c, direction))
        return fences
    
    def dfs(ufds, grid, r, c, group, curr_fences):
        if (r, c) in group:
            return
        group.add((r, c))
        
        curr = grid[r][c]
        for direction, (dr, dc) in enumerate(add):
            newr, newc = r + dr, c + dc
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == curr:
                # Join neighboring fences
                newfences = get_fence_ids(newr, newc)
                directions = [1, 3] if direction in [0, 2] else [0, 2]
                ufds.add_fences(newfences)
                ufds.bulk_union(curr_fences, newfences, directions)
                # DFS if unvisited
                if (newr, newc) not in group:
                    dfs(ufds, grid, newr, newc, group, newfences)
    
    price = 0
    visited = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if (r, c) not in visited:
                ufds = UFDS()
                group = set()
                fences = get_fence_ids(r, c)
                ufds.add_fences(fences)
                dfs(ufds, grid, r, c, group, fences)
                
                fences = ufds.get_num_fences()
                groupsize = len(group)
                price += fences * groupsize

                visited.update(group)
    print(price)

if __name__ == '__main__':
    puzzle_input = read_input()
    part1(puzzle_input)
    part2(puzzle_input)
