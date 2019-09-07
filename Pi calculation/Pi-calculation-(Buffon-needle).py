'''
Calculation of the Pi-number by throwing Buffon's needles
By Romanko Vladimir, July 2019.
'''
import numpy as np

class IGLA:
    def __init__(self, l, R):
        self.l=l
        self.R=R
    def brosanie(self):
        peresech=False
        h=np.random.uniform(0, self.R)
        alpha=np.random.uniform(0, np.pi/2)
        if (np.sin(alpha)*self.l/2 >= h) or (np.sin(alpha)*self.l/2 >= self.R-h):
            peresech=True
        return peresech
 
########               MAIN PROGRAM  
         
n=100000      # Needle throwing quantity (The number of iterations of the inner loop)
m=5       # The number of iterations of the outer loop      
L=5        # Needle's length
r=7      # Distance between parallel lines

ig1=IGLA(L,r)
arr=np.zeros(m)
for k in np.arange(m):
    n_peresech=0
    for i in np.arange(n):
        if ig1.brosanie():
            n_peresech+=1
    p=n_peresech/n
    PI=2*L/(r*p)
    arr[k]=PI
    
mo=arr.sum()/m
print("MO_of_Pi = ", mo)
mo_otkl=abs(mo-np.pi)
print("mo_otkl = ", mo_otkl)
arr2=(arr-np.pi)**2
std_otkl=np.sqrt(arr2.sum()/m)
print("arr2 = ", arr2)
print("std_otkl = ", std_otkl)

    
    
        
