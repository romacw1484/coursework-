from collections import deque


# Rewrite in my own words 
 
# Create a set to store visited nodes
# Create a queue to store nodes to visit
# Create a list to store the order of visited nodes

def bfs(graph, start):

    VisitedNodes = set()
    NodesToVisit = deque([start])
    Order =  []

    while NodesToVisit: 
        CurrentNode = NodesToVisit.popleft()
        if CurrentNode not in VisitedNodes:
            VisitedNodes.add(CurrentNode)
            Order.append(CurrentNode)
            for neighbor in graph[CurrentNode]:
                if neighbor not in VisitedNodes:
                    NodesToVisit.append(neighbor)
                    print("Enqueued:", neighbor)

    return Order


    

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Order:", bfs(graph, 'A'))

