# Graph: Topological Sort & Cycle Detection
from collections import defaultdict, deque

def topological_sort_kahn(graph, num_nodes):
    """Kahn's algorithm for topological sort"""
    in_degree = [0] * num_nodes
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque(i for i in range(num_nodes) if in_degree[i] == 0)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != num_nodes:
        return None  # Cycle detected
    return result

graph = defaultdict(list)
graph[5].extend([2, 0])
graph[4].extend([0, 1])
graph[2].append(3)
graph[3].append(1)
result = topological_sort_kahn(graph, 6)
print("Topological order:", result)
