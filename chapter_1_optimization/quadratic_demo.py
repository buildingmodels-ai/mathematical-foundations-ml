import numpy as np
import matplotlib.pyplot as plt

# Generate a symmetric positive definite matrix
np.random.seed(42)
B = np.random.randn(2, 2)
A = B.T @ B  # This ensures A is symmetric positive definite

def quadratic_function(x, A):
    return 0.5 * x.T @ A @ x

# Create grid
x1 = np.linspace(-3, 3, 200)
x2 = np.linspace(-3, 3, 200)
X1, X2 = np.meshgrid(x1, x2)

Z = np.zeros_like(X1)

for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        x = np.array([X1[i, j], X2[i, j]])
        Z[i, j] = quadratic_function(x, A)

# Plot contour
plt.figure(figsize=(6,6))
plt.contourf(X1, X2, Z, levels=50)
plt.title("Convex Quadratic Function")
plt.xlabel("x1")
plt.ylabel("x2")
plt.colorbar()
plt.tight_layout()
plt.savefig("quadratic_contour.png", dpi=300)
plt.show()
