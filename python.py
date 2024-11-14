# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 07:38:12 2024

@author: L13
"""

import random
import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted graph using NetworkX
graph = nx.Graph()

# Ask for the number of vertices
num_vertices = int(input("Enter the number of vertices: "))

# Generate vertices named x0 to xN
vertices = [f"x{i}" for i in range(num_vertices)]
graph.add_nodes_from(vertices)

# Add edges with positive random weights between 1 and 100 to avoid negative cycles
print("Adding edges with random weights between 1 and 100:")
for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
        weight = random.randint(1, 100)  # Range 1 to 100
        graph.add_edge(vertices[i], vertices[j], weight=weight)
        print(f"{vertices[i]} - {vertices[j]} : {weight}")

# Create the graph for visualization using NetworkX
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

# Display the graph
plt.title("Bellman-Ford Graph")
plt.axis('off')
plt.show()

# Ask for the start and end vertices for Bellman-Ford
start_vertex = input("Enter the starting vertex for Bellman-Ford (e.g., x0): ")
end_vertex = input("Enter the ending vertex for Bellman-Ford (e.g., x1): ")

# Verify the vertices exist in the graph
if start_vertex in graph.nodes() and end_vertex in graph.nodes():
    try:
        # Compute the shortest path with Bellman-Ford
        path = nx.bellman_ford_path(graph, start_vertex, end_vertex, weight='weight')
        distance = nx.bellman_ford_path_length(graph, start_vertex, end_vertex, weight='weight')

        print(f"Minimum distance from {start_vertex} to {end_vertex} : {distance}")
        print(f"Shortest path: {path}")
    except nx.NetworkXNoPath:
        print(f"No path found between {start_vertex} and {end_vertex}")
    except nx.NetworkXUnbounded:
        print("Negative cycle detected in the graph")
else:
    print("Invalid vertices. Please make sure both vertices exist in the graph.")

