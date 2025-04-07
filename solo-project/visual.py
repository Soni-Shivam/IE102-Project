import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math

def generate_random_graph(n, p, draw=True):
    G = nx.erdos_renyi_graph(n, p)
    
    num_edges = G.number_of_edges()
    degrees = [deg for node, deg in G.degree()]
    avg_degree = np.mean(degrees)
    clustering = nx.average_clustering(G)
    
    try:
        is_connected = nx.is_connected(G)
    except nx.NetworkXError:
        is_connected = False

    try:
        avg_shortest_path = nx.average_shortest_path_length(G) if is_connected else float('inf')
    except:
        avg_shortest_path = float('inf')

    largest_cc = max(nx.connected_components(G), key=len)
    giant_component_size = len(largest_cc)

    if draw:
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(4,4))
        nx.draw(G, pos, node_color='skyblue', with_labels=True, node_size=500)
        plt.title(f"G(n={n}, p={p})\nEdges: {num_edges}, Connected: {is_connected}")
        plt.show()

    results = {
        "num_edges": num_edges,
        "avg_degree": avg_degree,
        "clustering_coefficient": clustering,
        "is_connected": is_connected,
        "avg_shortest_path": avg_shortest_path,
        "giant_component_size": giant_component_size
    }
    
    return results

# Example usage
n = 100
p = 0.01
graph_stats = generate_random_graph(n, p)
graph_stats
