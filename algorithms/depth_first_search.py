# Depth First Search (DFS) on a graph
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_helper(start, visited, result)
        return result

    def _dfs_helper(self, node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, result)

g = Graph()
g.add_edge(0, 1); g.add_edge(0, 2)
g.add_edge(1, 3); g.add_edge(2, 4)
print("DFS from 0:", g.dfs(0))
