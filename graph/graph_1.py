class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[0]*vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        if 0 < v <= self.V and 0 <= u < self.V:
            self.adj[u][v] = weight
            self.adj[v][u] = weight  # For undirected graph
        else:
            print("Enter valid vertices")

    def remove_edge(self, u, v):
        if 0 <= v < self.V and 0 <= u < self.V:
            self.adj[u][v] = 0
            self.adj[v][u] = 0  # For undirected graph
    
    def has_edge(self, u, v):
        if 0 <= v < self.V and 0 <= u < self.V:
            return self.adj[u][v] == 1

    def display(self):
        for row in self.adj:
            print(row)

g1 = Graph(3)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(0, 2)
g1.display()
# print(g1.has_edge(2,3))
# Output:
