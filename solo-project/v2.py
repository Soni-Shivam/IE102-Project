import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Equation: beta = 1 - exp(-c * beta)
def giant_component_eq(beta, c):
    return beta - (1 - np.exp(-c * beta))

# Range of c values
c_values = np.linspace(0, 3, 100)
beta_values = []

# Solve for beta numerically for each c
for c in c_values:
    beta_initial_guess = 0.0001 if c < 1 else 0.5  # Better convergence
    beta_solution, = fsolve(giant_component_eq, beta_initial_guess, args=(c))
    beta_values.append(beta_solution)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(c_values, beta_values, label='β (Size of Giant Component)', color='blue')
plt.axvline(x=1, color='red', linestyle='--', label='Phase Transition (c = 1)')
plt.title('Size of the Giant Component vs c = np')
plt.xlabel('c = np (Average Degree)')
plt.ylabel('β (Fraction of Nodes in Giant Component)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("giant_component_vs_c.png")  # Save the plot
plt.show()
