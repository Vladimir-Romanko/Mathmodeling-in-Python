"""
GRADIENT DESCENT METHOD — Gradient descent with line search.
Without relying on pre-existing unconstrained optimization 
libraries, we will implement the "gradient descent with line search"
method for a two-dimensional function f(x, y) defined over
the entire plane (unconstrained optimization).
The step size is not fixed; instead, it is determined anew
at each iteration by solving a one-dimensional optimization 
problem along the direction of the negative gradient.
We solve this one-dimensional problem using symbolic
computation (the sympy library) by calculating the
derivative of the function along the negative gradient direction
and setting it to zero.

By Vladimir Romanko, November 2026
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.ticker as ticker

def func(x,y):
    # The function we want to minimize
    return x**2 + 3*y**2 - x - 2*y

def dx(x,y):
    # We calculate the partial derivative of func with respect to x
    return sp.diff(func(x,y),x)

def dy(x,y):
    # We calculate the partial derivative of func with respect to y
    return sp.diff(func(x,y),y)

def stop_condition(x_old, y_old):
    # The stopping condition: the gradient norm is smaller than epsilon
    c = sp.sqrt(dx(x,y)**2 + dy(x,y)**2)
    return c.evalf(3, subs = {x:x_old, y:y_old}) > epsilon

'''  MAIN PROGRAM  '''

x,y,alpha = sp.symbols('x,y,alpha')
x_old = 5;  y_old = 5 # The initial point from which we start gradient descent
# k -- iteration number, epsilon -- algorithm stopping criterion
k = 0;   epsilon = 0.02

list_x_new = [] # A list of all x-coordinate values at each iteration
list_y_new = [] # A list of all y-coordinate values at each iteration
list_alpha = [] # A list of all step size values at each iteration
list_func = [] # A list of all function values at each iteration

# The main loop of our algorithm, where k is the iteration number
while stop_condition(x_old, y_old):
    # a and b are the new x and y coordinates, respectively, depending on the variable alpha
    a = x_old - alpha * dx(x,y).evalf(subs = {x: x_old, y: y_old})
    b = y_old - alpha * dy(x,y).evalf(subs = {x: x_old, y: y_old})
    print('Iteration k =',k)
    print('a =', a)
    print('b =', b)
    # Next, we differentiate the function func and
    # solve the equation diff_func(a,b) = 0, obtaining a list of roots
    alpha_opt = sp.solve(sp.diff(func(a,b),alpha), alpha)
    print('List of alpha_opt =', alpha_opt)
    # Then we select the required root from the list, which must be greater than zero
    # -- the smallest positive root
    alpha_opt = min([i.evalf() for i in alpha_opt if i>0])
    print('alpha_opt_min =', alpha_opt)
    # We calculate the numerical values of the coordinates of the new point (x,y)
    x_new = x_old - alpha_opt * dx(x,y).evalf(subs = {x: x_old, y: y_old})
    y_new = y_old - alpha_opt * dy(x,y).evalf(subs = {x: x_old, y: y_old})
    x_old = x_new
    y_old = y_new
    print('x_new =', x_new, '  y_new =', y_new)
    print('func =', func(x_new, y_new))
    print('---------')
    list_x_new.append(x_new)
    list_y_new.append(y_new)
    list_alpha.append(alpha_opt)
    list_func.append(func(x_new, y_new))
    k += 1
    if k >= 50:
        print('The loop was interrupted by a break')
        break

# Visualization
fig = plt.figure(figsize = (20,7))
ax1 = fig.add_axes([0,0,0.7,1], projection = '3d')
ax2 = fig.add_axes([0.6,0.08,0.35,0.8])   
x_val = np.linspace(-4,4,150)
y_val = np.linspace(-4,4,150)
x_arg, y_arg = np.meshgrid(x_val, y_val)

ax1.plot_surface(x_arg,y_arg,func(x_arg,y_arg), rstride = 1, cstride = 1, cmap = 'RdGy')
ax1.tick_params(axis = 'both', labelsize = 22)

level = sorted(list_func)
ax1.contour(x_arg,y_arg, func(x_arg,y_arg), zdir = 'z',
            offset = -20, cmap = 'RdGy', levels = level)
ax1.zaxis.set_major_locator(ticker.MultipleLocator(50))
ax1.text(4.5,6,70, 'func(x,y)', size = 22)
ax1.text(1.5,-9.5,0, 'x', size = 22)
ax1.text(8.5,-3,0, 'y', size = 22)

ax2.contour(x_arg,y_arg, func(x_arg,y_arg),
            cmap = 'RdGy', levels = level)
ax2.plot(list_x_new, list_y_new, color ='green', linestyle = '--')