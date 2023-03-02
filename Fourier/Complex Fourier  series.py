'''
Approximation of functions of one variable by Fourier
series in complex form.
We define a real function f(x) and build its graph.
On the same graph, we build an approximation of this
function by a complex-valued Fourier series.
Although the series is complex, its sums are always real.

It can be seen that for a sufficiently large number
of terms in the Fourier series, the function approximates well.
This is true for all but the most extreme points (-pi and pi).
         By Vladimir Romanko, February 2023.
'''
import numpy as np
import matplotlib.pyplot as plt
import time
import sympy as sp

'''            PARAMETERS          '''
nmax = 6   # Number of terms in the Fourier series
ymin = -np.pi   # Domain of a function
ymax = np.pi
ny = 10  #  The number of segments into which
         #  we divide the domain of the function
func = np.zeros(ny)  # The values of the
                     # sums of the Fourier series

'''            MAIN PROGRAM          '''
t1 = time.time()

x = sp.symbols('x', real = True)
y = np.linspace(ymin,ymax,ny)  
f = sp.exp(x)   # This is our function - exponent
real_f = np.exp(y)  # This is our function - exponent

for k in np.arange(0, ny):
    summa = 0
    for n in np.arange(0,nmax + 1):
        if n != 0: 
            Int = sp.integrate( f * sp.exp(-sp.I*n*x), (x,-sp.pi,sp.pi) )
            cn = Int / (2*sp.pi)
            summa += cn * sp.exp(sp.I*n*x) + cn.conjugate() * sp.exp(sp.I*(-n)*x)      
        else:
            Int = sp.integrate( f * sp.exp(-sp.I*n*x), (x,-sp.pi,sp.pi) )
            cn = Int / (2*sp.pi)
            summa += cn * sp.exp(sp.I*n*x)  
            
    sum_subs = summa.subs(x,y[k])
    func[k] = sp.re( sum_subs.evalf() )
    
plt.figure( figsize=(12,9) )  
plt.plot(y, func, label = 'Fourier', marker = '', lw = 1, ls = '-')
plt.plot(y, real_f, label = 'Real function', marker = '', lw = 1.7, ls = ':')
plt.title('Fourier approximation in complex form')
plt.xlabel('y')
plt.ylabel('Functions')
plt.xlim((-ymax, ymax))
plt.legend(loc='upper left')
plt.grid()
plt.show()        

t2 = time.time()    
print('Task execution time =', t2 - t1, 'seconds')