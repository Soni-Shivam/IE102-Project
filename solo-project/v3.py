import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters for n = 100
n_small = 100
trials = 5000
p_values_small = np.linspace(0.005, 0.1, 50)
connectivity_probs_small = []

# Check connectivity across multiple trials
for p in p_values_small:
    connected_count = 0
    for _ in range(trials):
        G = nx.erdos_renyi_graph(n_small, p)
        if nx.is_connected(G):
            connected_count += 1
    connectivity_probs_small.append(connected_count / trials)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(p_values_small, connectivity_probs_small, marker='o', linestyle='-', color='green')
plt.axvline(x=np.log(n_small)/n_small, color='red', linestyle='--', label=f'Threshold ≈ ln(n)/n ≈ {np.log(n_small)/n_small:.4f}')
plt.title('Connectivity in Erdős–Rényi Graph G(n, p) for n=100')
plt.xlabel('p (Edge Probability)')
plt.ylabel('Probability of Connectivity')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()