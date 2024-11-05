import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def printMST(self, parent):
        print("\nEdge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")

    def primMST(self):
        key, parent = [sys.maxsize] * self.V, [-1] * self.V
        key[0], mstSet = 0, [False] * self.V

        for _ in range(self.V):
            u = min((key[i], i) for i in range(self.V) if not mstSet[i])[1]
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v], parent[v] = self.graph[u][v], u

        self.printMST(parent)

def input_graph():
    vertices = int(input("\nEnter the number of vertices: "))
    g = Graph(vertices)

    print("Enter the adjacency matrix (row by row):")
    for i in range(vertices):
        g.graph[i] = list(map(int, input(f"Row {i + 1}: ").split()))

    g.primMST()

input_graph()