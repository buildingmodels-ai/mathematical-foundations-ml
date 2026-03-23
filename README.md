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

Key concepts:

- Linear systems \( Xw = y \)
- Overdetermined problems
- Least squares formulation
- Derivation of the normal equations
- Orthogonal projection onto column space
- Rank condition and invertibility of \( X^T X \)
- Moore–Penrose pseudo-inverse
- Numerical stability and condition number

The chapter connects linear algebra, geometry, and optimization theory.

A Python implementation illustrates:

- Closed-form least squares solution
- Comparison with NumPy's `lstsq`
- Verification of orthogonality of the residual
- Computation of the condition number
