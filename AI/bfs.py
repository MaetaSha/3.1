graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}

def bfs(graph, start):
    visited = []  # List to keep track of visited nodes
    queue = [start]  # Initialize a queue

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)

    return visited
print(bfs(graph, 'A'))
