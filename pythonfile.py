import numpy as np
import matplotlib.pyplot as plt

# Define matrix A
A = np.array([[-2, 1],
              [1, 0]])

# Define function handles for u and v
def u(x, y):
    return A[0, 0] * x + A[0, 1] * y

def v(x, y):
    return A[1, 0] * x + A[1, 1] * y

# Create grid
xx = np.linspace(-4, 4, 500)
yy = np.linspace(-4, 4, 500)
XX, YY = np.meshgrid(xx, yy)

# Calculate u and v on the grid
UU = u(XX, YY)
VV = v(XX, YY)

# Plot streamlines
plt.figure(10)
plt.clf()
plt.streamplot(XX, YY, UU, VV, density=1)

# Plot invariant axes
eigenvalues, eigenvectors = np.linalg.eig(A)
v1 = eigenvectors[:, 0]
v2 = eigenvectors[:, 1]
plt.plot(xx, (xx * v1[1] / v1[0]), 'r', linewidth=2)
plt.plot(xx, (xx * v2[1] / v2[0]), 'r', linewidth=2)

# Plot equilibrium point
plt.plot(0, 0, '.k', markersize=20)

plt.axis('equal')
plt.axis([min(xx), max(xx), min(yy), max(yy)])
plt
