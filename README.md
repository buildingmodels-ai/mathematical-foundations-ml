# mathematical-foundations-ml
Mathematical foundations for machine learning, including optimization, linear algebra and probability, with theoretical derivations and Python illustrations.

# Mathematical Foundations for Machine Learning
This repository documents my study of the mathematical foundations required for modern machine learning.

The goal is to connect rigorous theoretical derivations with practical Python implementations.

The topics are structured progressively and focus on core pillars of machine learning:

- Optimization and Convexity
- Linear Algebra for Machine Learning
- Eigenvalues and Dimensionality Reduction
- Probability and Statistical Foundations

Each chapter contains:
- Theoretical explanations
- Mathematical derivations
- Links with machine learning concepts
- Python illustrations and simulations

---

## Chapter 1 — Optimization & Quadratic Forms
This chapter introduces quadratic forms, gradients, Hessians, and convexity conditions.

Key concepts:
- Quadratic functions: $f(x) = \frac{1}{2} x^T A x$
- Gradient computation
- Hessian matrix
- Convexity and positive semi-definite matrices
- Relation between eigenvalues and convexity

Theoretical results are supported with numerical examples in Python.

---

## Chapter 2 — Linear Algebra & Least Squares
This chapter develops the linear algebra foundations of least squares regression and its geometric interpretation.

It focuses on solving overdetermined linear systems and understanding the role of projections in optimization.

### Core Problem

We study linear systems of the form:

$$
Xw = y
$$

When the system is overdetermined ($n > d$), we solve:

$$
\min_{w \in \mathbb{R}^d} \|Xw - y\|^2
$$

### Key Concepts

- Linear systems
- Overdetermined problems
- Least squares formulation
- Derivation of the normal equations:

$$
X^T X w = X^T y
$$

- Orthogonal projection onto the column space of $X$
- Rank condition and invertibility of $X^T X$
- Moore–Penrose pseudo-inverse
- Numerical stability and condition number

### Python Illustration

The chapter includes a numerical implementation showing:

- Closed-form least squares solution
- Comparison with NumPy's `lstsq`
- Verification that:

$$
X^T (y - Xw^*) = 0
$$

- Computation of the condition number

---

## Chapter 3 — Eigenvalues & Principal Component Analysis

This chapter develops the spectral foundations of dimensionality reduction.

It introduces eigenvalues, orthogonal diagonalization, and their central role in Principal Component Analysis (PCA).

### Core Concepts
- Eigenvalues and eigenvectors:  
  $A v = \lambda v$

- Spectral theorem for symmetric matrices:  
  $A = Q \Lambda Q^T$

- Covariance matrix:  
  $\Sigma = \frac{1}{n} X^T X$

- PCA as a constrained optimization problem:  
  $\max_{\|v\|=1} v^T \Sigma v$

leading to:

$\Sigma v = \lambda v$

### Geometric Interpretation
The principal components define orthogonal directions of maximal variance.

Projection onto the first $k$ components:  
$Z = X V_k$

### Python Illustration
The chapter includes:

- Computation of the covariance matrix  
- Eigendecomposition  
- Projection onto the first principal component  
- Visualization of principal directions  

This chapter connects linear algebra, optimization, and statistical learning theory.
