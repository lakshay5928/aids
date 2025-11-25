graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(start):
    visited = set()
    stack = [start]   

    while stack:
        node = stack.pop()   
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

print("DFS Traversal starting from node A:")
dfs('A')