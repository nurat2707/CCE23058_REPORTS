class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x 
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self):
        result = []
        self.graph.sort(key=lambda x: x[2])
        parent = list(range(self.V))
        rank = [0] * self.V

        for u, v, w in self.graph:
            x, y = self.find(parent, u), self.find(parent, v)
            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        print("\nEdge \tWeight")
        for u, v, weight in result:
            print(f"{u} - {v}    {weight}")

def input_graph():
    vertices = int(input("\nEnter the number of vertices: "))
    g = Graph(vertices)

    g.graph = []
    print("Enter the adjacency matrix (row by row):")
    for i in range(vertices):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        for j in range(i + 1, vertices):
            if row[j] != 0:  
                g.add_edge(i, j, row[j])

    g.kruskal_mst()

input_graph()