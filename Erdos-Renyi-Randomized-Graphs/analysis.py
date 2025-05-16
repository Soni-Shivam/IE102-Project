import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters for the Erdos-Renyi model
n = 1000  # number of vertices
p = 0.4  # probability of edge creation

# Generate the random graph using Erdos-Renyi model
G = nx.erdos_renyi_graph(n, p)

# Get degrees of all vertices
degrees = [G.degree(i) for i in G.nodes()]

# Plot the degree distribution
plt.figure(figsize=(8, 6))
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2), alpha=0.75, color='blue', edgecolor='black')
plt.title('Degree Distribution of an Erdos-Renyi Graph')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
