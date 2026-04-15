import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ----- Generate correlated 2D data -----
n = 300

x1 = np.random.randn(n)
x2 = 2 * x1 + 0.5 * np.random.randn(n)

X = np.column_stack((x1, x2))

# Center data
X_mean = np.mean(X, axis=0)
X_centered = X - X_mean

# ----- Covariance matrix -----
Sigma = (1/n) * X_centered.T @ X_centered

# ----- Eigen decomposition -----
eigenvalues, eigenvectors = np.linalg.eig(Sigma)

# Sort by descending eigenvalue
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# ----- Projection onto first principal component -----
v1 = eigenvectors[:, 0]
Z = X_centered @ v1

# ----- Visualization -----
plt.figure(figsize=(6,6))
plt.scatter(X_centered[:,0], X_centered[:,1], alpha=0.4)
plt.quiver(0, 0, v1[0], v1[1], 
           scale=3, color='red', width=0.01)

plt.title("PCA - First Principal Component")
plt.axis("equal")
plt.show()

print("Eigenvalues:")
print(eigenvalues)
