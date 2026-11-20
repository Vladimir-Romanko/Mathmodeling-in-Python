# Gradient Descent with Symbolic Line Search (2D)

## Overview

This is an educational Python implementation of a gradient-based method for unconstrained optimization of a two-dimensional function:

$$
\min_{(x,y)\in\mathbb{R}^2} f(x,y).
$$

**In plain words:** the goal is to find values of `x` and `y`, anywhere in the two-dimensional plane, that make the function `f(x, y)` as small as possible.

The algorithm uses the negative gradient as the search direction. The step size is recalculated at every iteration by constructing a one-dimensional function along that direction and solving its first-order stationarity equation symbolically with **SymPy**.

The implementation does not rely on ready-made general-purpose unconstrained optimization routines. It uses symbolic differentiation and equation solving, while NumPy and Matplotlib are used for numerical calculations and visualization.

## How the algorithm works

At iteration `k`, the gradient is evaluated at the current point:

$$
\nabla f(x_k,y_k)=
\begin{pmatrix}
 f_x(x_k,y_k)\\
 f_y(x_k,y_k)
\end{pmatrix}.
$$

**In plain words:** the gradient is a vector with two components. The first is the partial derivative with respect to `x`, and the second is the partial derivative with respect to `y`. These components describe the direction of the steepest local increase of the function. The algorithm moves in the opposite direction, where the function initially decreases.

The next point is parameterized along the negative-gradient direction:

$$
\begin{aligned}
 x(\alpha)&=x_k-\alpha f_x(x_k,y_k),\\
 y(\alpha)&=y_k-\alpha f_y(x_k,y_k),
\end{aligned}
\qquad \alpha>0.
$$

**In plain words:** starting from the current point `(x_k, y_k)`, the algorithm moves opposite to the gradient. The parameter `alpha` controls the step length. The gradient components are evaluated at the current point and are kept fixed while `alpha` varies.

This defines a one-dimensional function:

$$
\varphi_k(\alpha)=f\bigl(x(\alpha),y(\alpha)\bigr).
$$

**In plain words:** instead of optimizing over both `x` and `y` at once, the algorithm considers only points on the ray defined by the negative-gradient direction. The function `phi_k(alpha)` gives the objective-function value at each point on that ray.

The code differentiates this one-dimensional function with respect to `alpha` and solves:

$$
\varphi_k'(\alpha)=0.
$$

**In plain words:** SymPy finds step sizes at which the derivative along the search direction is zero. From the positive real roots returned by SymPy, the code selects the smallest one. This is a stationary point of the one-dimensional function; it is not necessarily a minimum.

The selected value is used as the step size for the next iteration:

$$
(x_{k+1},y_{k+1})=
\bigl(x(\alpha_k),y(\alpha_k)\bigr).
$$

**In plain words:** the algorithm updates both coordinates using the selected step size and the negative gradient calculated at the previous point.

The iterations stop when the gradient norm falls below the specified tolerance:

$$
\|\nabla f(x_k,y_k)\|_2 < \varepsilon.
$$

**In plain words:** the algorithm stops when the length of the gradient vector becomes smaller than `epsilon`, or when the iteration limit is reached. A small gradient indicates a stationary point or a point close to one; it does not, by itself, prove that the point is a minimum.

## What the implementation is intended for

The project demonstrates how gradient descent and a symbolic one-dimensional search can be combined for unconstrained optimization in $\mathbb{R}^2$.

It can be applied to many sufficiently smooth functions that:

- can be expressed using operations and functions understood by SymPy;
- have symbolic partial derivatives that SymPy can calculate;
- produce a directional-derivative equation that SymPy can solve and whose positive real roots can be compared.

The method is not restricted to quadratic functions. However, the fact that a function is twice differentiable does **not**, by itself, guarantee that this particular symbolic implementation can solve the resulting equation.

## Important limitations

1. **No guarantee of finding a global minimum.** This is a local, starting-point-dependent iterative method. Its result depends on the initial point and the shape of the objective function. It may converge to a local minimum or to another stationary point; it does not search the entire plane for the global minimum.

2. **The selected step is not guaranteed to minimize the function along the search ray.** The code selects the smallest positive solution of $\varphi_k'(\alpha)=0$. A stationary point of the one-dimensional function may be a local minimum, a local maximum, or a stationary inflection point. The code does not check the second derivative, verify a change of sign in the first derivative, or compare all candidate values of $\varphi_k$. Therefore, the selected step is not necessarily an exact line-search minimizer and does not necessarily decrease the objective function.

3. **A positive stationary step must be found at each iteration.** If SymPy returns no positive root, the current implementation cannot select a step: applying `min()` to an empty list raises an error. Some functions may have no positive stationary point along the current negative-gradient ray.

4. **A minimum may not exist.** If the objective function is unbounded below or does not attain a minimum, convergence to a minimizer cannot be expected. The algorithm has no mechanism for handling this situation. Depending on the function, it may fail to find a step, move away, or encounter a stationary point that is not a minimum.

5. **Symbolic solvability is a practical restriction.** Many differentiable functions do not lead to equations that SymPy can solve in closed form. SymPy may return no usable roots, an incomplete set of roots, or expressions whose positivity cannot be determined automatically. Thus, the implementation is suitable for a broad class of symbolic examples, not for every twice-differentiable function.

6. **A small gradient does not classify the stationary point.** The stopping condition checks the gradient norm only. A point with a zero or sufficiently small gradient can be a local minimum, a local maximum, or a saddle point. Classifying the result requires additional analysis, for example by examining the Hessian.

7. **The current implementation is two-dimensional and has a fixed iteration cap.** It is written specifically for functions of `x` and `y`, and the main loop stops after at most 50 iterations. The stopping test currently evaluates the gradient norm with `evalf(3)`, i.e. to three significant decimal digits, which limits the precision of that test.

8. **The objective function is also used for plotting.** In addition to accepting SymPy symbols for symbolic differentiation, the current plotting code passes NumPy arrays to `func`. A replacement function must therefore be compatible with both kinds of inputs, or the plotting code must be adapted (for example, by using `sympy.lambdify`).

## Requirements

- Python 3
- NumPy
- SymPy
- Matplotlib

## Running the project

1. Install the required libraries.
2. Run the Python script.
3. To test another objective function, edit `func(x, y)`.
4. Adjust the initial point (`x_old`, `y_old`) and the stopping tolerance (`epsilon`) as needed.

The script prints the iteration information and displays the objective-function surface together with a contour plot showing the sequence of iterates.

## Project purpose

This project is intended for learning and experimentation. Its main purpose is to illustrate the negative-gradient search direction, symbolic differentiation, and the construction of a one-dimensional step-selection problem. It should not be treated as a robust general-purpose optimizer without additional safeguards and a more reliable line-search procedure.
