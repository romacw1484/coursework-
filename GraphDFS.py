from collections import deque

def DFS(graph, start, visited=None, order=None):
    
    if visited is None: # it will be
        visited = set()
    if order is None: # it will be
        order = []
        
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order



# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


print("DFS Order:", dfs(graph, 'A'))
