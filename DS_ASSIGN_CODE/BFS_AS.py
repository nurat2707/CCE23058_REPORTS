# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:59:34 2024

@author: RAVICHANDRAN
"""

from collections import deque

# BFS Traversal with path
def BFS(graph, start):     
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    path = [start]  # To store the traversal path
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path.append(neighbor)
    
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
    print("1. BFS 2. exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        graph, directed = input_graph()
        start_vertex = input("Enter the start vertex: ")

        print("\nBFS Traversal")
        bfs_path = BFS(graph, start_vertex)
        print("Path taken in BFS: ", " -> ".join(bfs_path))
    elif ch==2:
        print("terminating")
        break
    else:
        print("invalid option")

    