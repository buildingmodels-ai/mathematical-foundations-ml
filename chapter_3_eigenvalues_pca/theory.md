# Chapter 3 — Eigenvalues & Principal Component Analysis (PCA)

## 1. Eigenvalues and Eigenvectors
Let $A \in \mathbb{R}^{d \times d}$ be a square matrix.

A nonzero vector $v \in \mathbb{R}^d$ is called an eigenvector of $A$ if there exists a scalar $\lambda \in \mathbb{R}$ such that:

$$
A v = \lambda v
$$

The scalar $\lambda$ is the associated eigenvalue.

### Geometric Interpretation
Eigenvectors define invariant directions of the linear transformation $A$.  
Applying $A$ stretches or compresses these directions by a factor $\lambda$.

If $A$ is symmetric:
- All eigenvalues are real
- Eigenvectors corresponding to distinct eigenvalues are orthogonal

---

## 2. Spectral Theorem
If $A$ is symmetric, then:

$$
A = Q \Lambda Q^T
$$

where:
- $Q$ is an orthogonal matrix of eigenvectors
- $\Lambda$ is a diagonal matrix of eigenvalues

---

## 3. Covariance Matrix
Given centered data $X \in \mathbb{R}^{n \times d}$, the covariance matrix is:

$$
\Sigma = \frac{1}{n} X^T X
$$

Properties:
- $\Sigma$ is symmetric
- $\Sigma$ is positive semi-definite
- Eigenvalues represent variance along principal directions

---

## 4. Principal Component Analysis
PCA solves:

$$
\max_{\|v\|=1} v^T \Sigma v
$$

Using Lagrange multipliers, the solution satisfies:

$$
\Sigma v = \lambda v
$$

Thus, principal components are eigenvectors of the covariance matrix.

The first principal component corresponds to the largest eigenvalue.

---

## 5. Dimensionality Reduction
Keeping the first $k$ eigenvectors $V_k$, the projection is:

$$
Z = X V_k
$$

This gives a lower-dimensional representation preserving maximal variance.

---

## 6. Link with Machine Learning
PCA is used for:
- Feature extraction
- Noise reduction
- Data visualization
- Preprocessing before regression or classification
- Spectral methods
