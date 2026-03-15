# Breadth First Search (BFS) on a graph
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

g = Graph()
g.add_edge(0, 1); g.add_edge(0, 2)
g.add_edge(1, 3); g.add_edge(2, 4)
print("BFS from 0:", g.bfs(0))
