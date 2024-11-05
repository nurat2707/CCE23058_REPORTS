# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:13:00 2024

@author: RAVICHANDRAN
"""

def floyd_warshall(graph, vertices):
    # Initialize distance matrix with infinity
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}
    
    # Set the distance from each vertex to itself as 0
    for v in vertices:
        dist[v][v] = 0
    
    # Populate initial distances based on the given graph edges
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            dist[vertex][neighbor] = weight
    
    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def user_input():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    vertices = []

    for i in range(n):
        vertex = input("\nEnter the vertex: ")
        vertices.append(vertex)
        neighbors = []
        m = int(input(f"Enter the number of edges for {vertex}: "))

        for j in range(m):
            neighbor = input(f"Enter neighbor of {vertex}: ")
            weight = int(input(f"Enter weight for edge {vertex} -> {neighbor}: "))
            neighbors.append((neighbor, weight))

        graph[vertex] = neighbors

    return graph, vertices

def print_distances(dist, vertices):
    print("\nAll-Pairs Shortest Paths:")
    for i in vertices:
        for j in vertices:
            if dist[i][j] == float('inf'):
                print(f"{i} -> {j}: No Path")
            else:
                print(f"{i} -> {j}: {dist[i][j]}")

graph, vertices = user_input()
distances = floyd_warshall(graph, vertices)
print_distances(distances, vertices)
