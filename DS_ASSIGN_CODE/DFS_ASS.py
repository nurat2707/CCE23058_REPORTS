from collections import deque


# DFS Traversal with path
def DFS(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited, path)
    
    return path

# Function to create input graph
def input_graph():
    graph = {}
    num_vertexs = int(input("Enter the number of vertices in the graph: "))
    directed = input("Is the graph directed? (yes/no): ").strip().lower() == 'yes'
    
    for _ in range(num_vertexs):
        vertex = input("Enter the vertex: ")
        graph[vertex] = []
        num_edges = int(input(f"Enter the number of edges from vertex {vertex}: "))
        for _ in range(num_edges):
            neighbor = input("Enter the neighbor: ")
            graph[vertex].append(neighbor)
            
            # For undirected graphs, add the reverse edge
            if not directed:
                if neighbor not in graph:
                    graph[neighbor] = []
                graph[neighbor].append(vertex)
    
    return graph, directed


# Main Execution
while True:
    print("1. DFS 2. exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        graph, directed = input_graph()
        start_vertex = input("Enter the start vertex: ")

        print("\nDFS Traversal")
        dfs_path = DFS(graph, start_vertex)
        print("Path taken in BFS: ", " -> ".join(dfs_path))
    elif ch==2:
        print("terminating")
        break
    else:
        print("invalid option")
