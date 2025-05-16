# epidemic_spread.py

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# Parameters
n = 1000  # number of nodes
p = 0.01  # probability of edge creation
initial_infected_fraction = 0.01
infection_prob = 0.03
recovery_prob = 0.01
timesteps = 100

# Create an Erdős–Rényi graph
G = nx.erdos_renyi_graph(n, p)

# Initialize states: S, I, R
states = {node: 'S' for node in G.nodes}
initial_infected = random.sample(G.nodes(), int(n * initial_infected_fraction))
for node in initial_infected:
    states[node] = 'I'

susceptible_counts = []
infected_counts = []
recovered_counts = []

# Simulation loop
for t in range(timesteps):
    new_states = states.copy()
    
    for node in G.nodes:
        if states[node] == 'I':
            # Try to infect neighbors
            for neighbor in G.neighbors(node):
                if states[neighbor] == 'S' and random.random() < infection_prob:
                    new_states[neighbor] = 'I'
            # Try to recover
            if random.random() < recovery_prob:
                new_states[node] = 'R'
    
    states = new_states

    # Count states
    s = list(states.values()).count('S')
    i = list(states.values()).count('I')
    r = list(states.values()).count('R')

    susceptible_counts.append(s)
    infected_counts.append(i)
    recovered_counts.append(r)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(susceptible_counts, label="Susceptible", color='blue')
plt.plot(infected_counts, label="Infected", color='red')
plt.plot(recovered_counts, label="Recovered", color='green')
plt.xlabel("Time Step")
plt.ylabel("Number of Nodes")
plt.title("Epidemic Spread on Erdős–Rényi Graph (SIR Model)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
