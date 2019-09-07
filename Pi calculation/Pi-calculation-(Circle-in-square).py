'''
Calculation of the Pi-number by throwing dots into a square circumscribed around a circle.
By Romanko Vladimir, July 2019.
'''
import numpy as np

class VNESH:  # Outer loop
    def __init__(self,m_iter):
        self.m_iter=m_iter
    def run_cycle(self):
        vnu2=VNUTR(storona, n)
        ar=np.zeros((self.m_iter,n))
        for k in np.arange(self.m_iter):
            ar=vnu2.pi_compute(ar,k)
        return ar
    def __repr__(self):
        str1=str(self.m_iter)+" iterations of calculating the number Pi at the side of the square "
        str2=str(storona)+" and number of points "+str(n)
        return str1+str2

class VNUTR:     #  Inner loop
    def __init__(self, a, n_square):
        self.a=a
        self.n_square=n_square
    def pi_compute(self, arr,kk):
        n_circ=0
        for i in np.arange(self.n_square):
            x=np.random.uniform(-self.a/2,self.a/2)
            y=np.random.uniform(-self.a/2,self.a/2)
            arr[kk,i]=x**2+y**2
        return arr
    def __repr__(self):
        str1="The calculation of the number Pi at the side of the square "+str(self.a)
        str2=" and number of points "+str(self.n_square)
        return str1+str2     

class VYVOD:    # Count aggregated statistics and display
    def __init__(self, mass):
        self.mass=mass; self.m=mass.shape[0];  self.n=mass.shape[1]
        self.mass_dim1=np.zeros(self.m)
        i=0
        for stroka in self.mass:
            n_circ=0
            for el in stroka:
                if el<=storona**2/4:
                    n_circ+=1
            self.mass_dim1[i]=4*n_circ/self.n
            i+=1
    def mo(self):
        return self.mass_dim1.sum()/self.m
    def mo_otkl(self, mo):
        return abs(mo-np.pi)
    def std_otkl(self):
        s=0
        for i in self.mass_dim1:
            s+=(i-np.pi)**2
        return np.sqrt(s/self.m) 


"""                      MAIN PROGRAM    """

n=3000   # the number of points to be squared in one iteration of the outer loop
m=100      # number of iterations of the outer loop
storona=1     # side length of a square
vne=VNESH(m)
arr=vne.run_cycle()
vyv=VYVOD(arr)
print(vne)
mo=vyv.mo()
print("MO_of_Pi = ", mo)
print("MO_OTKL = ", vyv.mo_otkl(mo))
print("STD_OTKL = ", vyv.std_otkl())