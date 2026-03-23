import numpy as np

# Reproducibility
np.random.seed(42)

# Generate synthetic data
n = 100  # number of samples
d = 3    # number of features

X = np.random.randn(n, d)

true_w = np.array([2.0, -1.5, 0.5])
noise = 0.1 * np.random.randn(n)

y = X @ true_w + noise


# ----- Closed-form least squares solution -----

XtX = X.T @ X
Xty = X.T @ y

w_closed = np.linalg.solve(XtX, Xty)

print("Closed-form solution:")
print(w_closed)


# ----- NumPy built-in least squares -----

w_lstsq, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)

print("\nNumPy lstsq solution:")
print(w_lstsq)


# ----- Check orthogonality of residual -----

residual_vector = y - X @ w_closed

orthogonality_check = X.T @ residual_vector

print("\nX^T r (should be close to zero):")
print(orthogonality_check)


# ----- Condition number -----

condition_number = np.linalg.cond(XtX)

print("\nCondition number of X^T X:")
print(condition_number)
