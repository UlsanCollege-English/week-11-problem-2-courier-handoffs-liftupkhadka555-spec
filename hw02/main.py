from collections import deque

def bfs_path(graph, s, t):
    if s not in graph or t not in graph:
        return None
    if s == t:
        return [s]

    visited = set([s])
    parent = {s: None}
    queue = deque([s])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
                if neighbor == t:
                    path = [t]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path
    return None
