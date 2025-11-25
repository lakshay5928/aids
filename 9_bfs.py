#to implement breadth first search algorithm for graph traversal
from collections import deque

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

def bfs(start):
    visited=set()   #to keep the track of visited node(avoid repeption)
    queue=deque({start}) #initialize the queue with start node
    
    #loop until queue become empty
    while queue:
        node=queue.popleft()   #remove first element from queue
        if node not in visited:  #if the node is not already visited
            print(node,end=" ")  #print the node (traversal order)
            visited.add(node)   #mark the node as visited
            queue.extend(graph[node]) #add all neighbours of this node into the queue
            
#call the bfs function            
print("BFS traversal starting from node A:")
bfs('A')