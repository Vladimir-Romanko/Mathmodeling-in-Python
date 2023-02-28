'''
Approximation of functions of one variable by Fourier series
in real form.
We define a real function f(x) and build its graph.
On the same graph, we build an approximation of this
function by a Fourier series.

It can be seen that for a sufficiently large
number of terms in the Fourier series, the function
approximates well. This is true for all but the most
extreme points (-pi and pi).
         By Vladimir Romanko, February 2023.
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as ing

'''            PARAMETERS          '''
ymin = -np.pi    # Domain of a function
ymax = np.pi
ny = 100  #  The number of segments into which
         #  we divide the domain of the function
summa = np.zeros(ny, dtype = float) # The values of the
                                   # sums of the Fourier series
imax = 20  # Number of terms in the Fourier series

'''            MAIN PROGRAM          '''
def f(x):   # This is our function - exponent
    return np.exp(x)

def fcos(x,i):
    return f(x) * np.cos(i*x)

def fsin(x,i):
    return f(x) * np.sin(i*x)

y = np.linspace(ymin, ymax, ny, dtype = float)
real_f = np.exp(y) # This is our function - exponent
v, err = ing.quad(f,ymin,ymax)
a0 =  v / (2*np.pi)  

for i in np.arange(1,imax + 1, dtype = int):
    v, err = ing.quad(fcos,ymin,ymax, args = i)
    ai = v / np.pi
    v, err = ing.quad(fsin,ymin,ymax, args = i)
    bi = v / np.pi
    summa += ai * np.cos(i*y) + bi * np.sin(i*y)

func = summa + a0

plt.figure(figsize=(12,9))  
plt.plot(y, func, label = 'Fourier', marker = '', lw = 1, ls = '-')
plt.plot(y, real_f, label ='Real function', marker = '', lw = 1.7, ls = ':')
plt.title('Fourier approximation')
plt.xlabel('y')
plt.ylabel('Functions')
plt.xlim((-ymax, ymax))
plt.legend(loc='upper left')
plt.grid()
plt.show()                                                