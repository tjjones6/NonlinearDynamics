import numpy as np
import matplotlib.pyplot as plt

# Define parameters
x = np.linspace(-2, 2, 500)
k = np.linspace(-1, 2, 500)
r = 0.52

# Create meshgrid
X, K = np.meshgrid(x, k)

# Define the function
F_1 = r * X * (1 - X / K) - (X ** 2) / (1 + X ** 2)

# Plot contour
plt.contour(K, X, F_1, levels=[0], colors='black')
plt.title(r'Bifurcation Diagram for $\dot{x} = rx(1 - \frac{x}{k}) - \frac{x^2}{1+x^2}$', fontsize=14)
plt.xlabel('k', fontsize=12)
plt.ylabel('x', fontsize=12)
plt.grid(True)
plt
