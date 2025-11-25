import heapq
def a_star(start, goal, graph, heuristic):
    # Priority queue stores: (f = g+h, g, current_node, path_taken)
    queue = [(heuristic[start], 0, start, [])]
    visited = set() # to track visited nodes

    # loop until queue become empty
    while queue:
        est_total, cost_so_far, node, path = heapq.heappop(queue)

        # Skip visited nodes
        if node in visited:
            continue

        # Mark node as visited
        visited.add(node)  
        path = path + [node]  # add current node to path

        # If goal reached → return path
        if node == goal:
            return path

        # Explore neighbors
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                new_cost = cost_so_far + edge_cost  #g(n) path cost so far
                est = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                #push neighbour into priorty queue with updated cost and path
                heapq.heappush(queue, (est, new_cost, neighbor, path))

    return None  # No path found
# Example graph (Adjacency list with edge costs)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}
# Example heuristic values (estimated cost to goal 'F')
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 2,
    'F': 0
}
print("A* path from A to F")
print(a_star('A','F',graph,heuristic))  # Output: ['A', 'B', 'E', 'F']
