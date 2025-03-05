class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.adjacency_list:
            self.add_vertex(v1)
        if v2 not in self.adjacency_list:
            self.add_vertex(v2)
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def is_connected(self, start, target):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex == target:
                return True
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(self.adjacency_list[vertex]) - visited)
        return False

    def shortest_path(self, start, target):
        # Dictionary to keep track of the parent of each visited node
        predecessor = {start: None}
        queue = [start]
        
        # BFS loop
        while queue:
            vertex = queue.pop(0)
            if vertex == target:
                # Reconstruct the path from target to start
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = predecessor[vertex]
                return path[::-1]  # Reverse the path
            
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in predecessor:
                    predecessor[neighbor] = vertex
                    queue.append(neighbor)
                    
        # If target is not reachable
        return None

    def __str__(self):
        return str(self.adjacency_list)


# Example usage:
graph = Graph()
graph.add_edge("New York", "Boston")
graph.add_edge("Boston", "Chicago")
graph.add_edge("Chicago", "Denver")
graph.add_edge("Denver", "San Fran")
graph.add_edge("San Fran", "Los Angeles")
graph.add_edge("Chicago", "Houston")

print("Graph (Adjacency List):")
print(graph)

print("\nIs there a path from New York to Los Angeles?")
print(graph.is_connected("New York", "Los Angeles"))  # Expected: True

print("\nShortest path from New York to Los Angeles:")
print(graph.shortest_path("New York", "Los Angeles"))   # Expected: Shortest path as a list

print("\nShortest path from New York to Houston:")
print(graph.shortest_path("New York", "Houston"))       # Expected: Shortest path as a list
