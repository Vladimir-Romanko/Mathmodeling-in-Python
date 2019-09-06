'''
Calculation of the Pi-number using the Monte-Carlo method.
By Romanko Vladimir, July 2019.
'''
import numpy as np

class VNESH:  # Vneshniy cikl
    def __init__(self,m_iter):
        self.m_iter=m_iter
    def run_cycle(self):
        vnu2=VNUTR(storona, n)
        ar=np.zeros((self.m_iter,n))
        for k in np.arange(self.m_iter):
            ar=vnu2.pi_compute(ar,k)
        return ar
    def __repr__(self):
        str1=str(self.m_iter)+" итераций расчёта числа Пи при стороне квадрата "
        str2=str(storona)+" и числе точек "+str(n)
        return str1+str2

class VNUTR:     #  Vnutrenniy cikl
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
        str1="Расчёт числа Пи при стороне квадрата "+str(self.a)
        str2=" и числе точек "+str(self.n_square)
        return str1+str2     

class VYVOD:    # Подсчёт агрегированных статистик и вывод на экран
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

n=3000   # число точек, набрасываемых в квадрат за одну итерацию внешнего цикла
m=100      # число итераций внешнего цикла   
storona=1     # длина стороны квадрата
vne=VNESH(m); arr=vne.run_cycle()
vyv=VYVOD(arr)
print(vne);  mo=vyv.mo(); 
print("MO_of_Pi = ", mo); print("MO_OTKL = ", vyv.mo_otkl(mo))
print("STD_OTKL = ", vyv.std_otkl())