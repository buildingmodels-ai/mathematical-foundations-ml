# Chapter 2 — Linear Algebra & Least Squares

## 1. Linear Systems in Machine Learning
Many machine learning problems reduce to solving a linear system of the form

$$
X w = y
$$

where:

- $X \in \mathbb{R}^{n \times d}$ is the design matrix  
- $w \in \mathbb{R}^d$ is the parameter vector  
- $y \in \mathbb{R}^n$ is the observation vector  

In most practical situations, $n > d$.  
The system is overdetermined and does not admit an exact solution.

We therefore solve the optimization problem

$$
\min_{w \in \mathbb{R}^d} \|Xw - y\|^2.
$$

---

## 2. Least Squares Formulation
Define the loss function

$$
L(w) = \frac{1}{2} \|Xw - y\|^2
$$

Expanding:

$$
L(w) = \frac{1}{2} (Xw - y)^T (Xw - y)
$$

$$
= \frac{1}{2} (w^T X^T X w - 2 y^T X w + y^T y)
$$

---

## 3. Gradient and Normal Equations
The gradient is

$$
\nabla L(w) = X^T (Xw - y)
$$

At the optimum:

$$
\nabla L(w) = 0
$$

which gives the **normal equations**

$$
X^T X w = X^T y
$$

If $X^T X$ is invertible:

$$
w^* = (X^T X)^{-1} X^T y
$$

---

## 4. Geometric Interpretation
The least squares solution corresponds to the orthogonal projection of $y$ onto the column space of $X$.

The residual vector

$$
r = y - Xw^*
$$

satisfies

$$
X^T r = 0
$$

which means that the residual is orthogonal to the column space of $X$.

Thus,

$$
Xw^* = P_{\mathrm{col}(X)} y
$$

This interpretation connects optimization with linear algebra and subspace geometry.

---

## 5. Rank Condition
If

$$
\mathrm{rank}(X) = d
$$

then $X^T X$ is symmetric positive definite and invertible.

If $X$ is not full rank, one uses the Moore–Penrose pseudo-inverse:

$$
w^* = X^+ y
$$

computed via Singular Value Decomposition (SVD).

---

## 6. Link with Machine Learning
Least squares forms the foundation of:

- Linear regression  
- Ridge regression (regularized least squares)
- Kernel methods  
- Many convex optimization problems  

The spectral properties of $X^T X$ directly influence numerical stability and convergence speed of gradient-based methods.
