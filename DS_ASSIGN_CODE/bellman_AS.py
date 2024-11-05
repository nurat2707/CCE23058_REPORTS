# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:37:07 2024

@author: RAVICHANDRAN
"""

from collections import defaultdict

def bellman_ford(graph, vertices, destination):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[destination] = 0
    for _ in range(len(vertices) - 1):
        for vertex in graph:
            for neighbour, weight in graph[vertex]:
                if distances[vertex] != float('inf') and distances[vertex] + weight < distances[neighbour]:
                    distances[neighbour] = distances[vertex] + weight
    
    for vertex in vertices:
        if distances[vertex] == float('inf'):
            print(f"The vertex {vertex} is unreachable from the destination vertex {destination}.")
    
    return distances

def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    for vertex, neighbours in graph.items():
        for neighbour, weight in neighbours:
            reversed_graph[neighbour].append((vertex, weight))
    return reversed_graph

def user_input():
    graph = defaultdict(list)
    vertices = set()
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Enter the vertex: ")
        vertices.add(vertex)
        m = int(input(f"Enter the number of edges for vertex {vertex}: "))
        for _ in range(m):
            neighbour = input(f"Enter the neighbour for vertex {vertex}: ")
            weight = int(input(f"Enter the weight for the edge {vertex} -> {neighbour}: "))
            graph[vertex].append((neighbour, weight))
            vertices.add(neighbour)
    return graph, vertices

def display_distances(distances, destination):
    print(f"\nShortest distances to the destination ({destination}):")
    for vertex, distance in distances.items():
        if distance == float('inf'):
            print(f"Vertex {vertex} is unreachable.")
        else:
            print(f"Distance to vertex {vertex}: {distance}")

graph, vertices = user_input()
reversed_graph = reverse_graph(graph)
destination = input("\nEnter the destination vertex: ")
distances = bellman_ford(reversed_graph, vertices, destination)
display_distances(distances, destination)