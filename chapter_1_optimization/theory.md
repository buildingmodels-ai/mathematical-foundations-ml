# Chapter 1 — Optimization & Quadratic Forms

## 1. Quadratic Forms
A quadratic function in ℝⁿ can be written as:

$$
f(x) = \frac{1}{2} x^T A x
$$

where:
- \( x \in \mathbb{R}^n \)
- \( A \in \mathbb{R}^{n \times n} \) is a symmetric matrix

Quadratic forms play a central role in optimization and machine learning.

---

## 2. Gradient Computation
Let:

$$
f(x) = \frac{1}{2} x^T A x
$$

If \( A \) is symmetric, the gradient is:

$$
\nabla f(x) = A x
$$

If \( A \) is not symmetric, the general result is:

$$
\nabla f(x) = \frac{1}{2}(A + A^T)x
$$

---

## 3. Hessian Matrix
The Hessian matrix is:

$$
\nabla^2 f(x) = A
$$

Thus, the curvature of the function is fully determined by the matrix \( A \).

---

## 4. Convexity Condition
The function \( f \) is convex if and only if:

$$
x^T A x \geq 0 \quad \text{for all } x
$$

This holds if and only if the matrix \( A \) is positive semi-definite:

$$
A \succeq 0
$$

---

## 5. Link with Eigenvalues
Since \( A \) is a real symmetric matrix, it is diagonalizable in an orthonormal basis.

The function is convex if and only if all eigenvalues of \( A \) satisfy:

$$
\lambda_i \geq 0
$$

This shows that convexity is directly related to the spectral properties of the matrix.

---

## 6. Connection to Machine Learning
Quadratic forms appear naturally in many machine learning problems.

### Least Squares Regression
The loss function for linear regression can be written as:

$$
L(w) = \frac{1}{2} (Xw - y)^T (Xw - y)
$$

Expanding this expression leads to a quadratic form in \( w \).  
The convexity of the loss function ensures the existence of a global minimum.

### Optimization Perspective
When the Hessian matrix is positive definite, gradient-based optimization methods (such as gradient descent or Newton's method) are guaranteed to converge toward a unique global minimum.

This explains why convexity plays a central role in modern machine learning theory.
