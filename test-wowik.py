"""
TEST
"""
import numpy as np
import itertools

#lst = [c * 3 for c in 'list']
#print("lst =", lst)

def diff_symb(chislo):
    st=""
    string = str(chislo)
    for symb in string:
        if symb not in st:
            st+=symb
    if len(st)!=len(string):
        return False
    else:
        return True

def unique_pairs(n):
    for i in range(n):
        for j in range(n):
            if round(np.log(i)) == round(np.tan(j)):
                yield i,j

s = "testee"
#for i,j in unique_pairs(1000):
#    print(i,j)
    
#for i,j in [c,d for c,d in itertools.product(range(n),range(n))]:
#    print(i,j)    
#n=10    
#for i in [c for c in s if c == "L"]:
#    print(i)        
#for i,j in [(i,j) for i in range(len(s)) for j in range(i+1, len(s))]: 
#    if s[i] == s[j]:
#        print(i,j,"    ",s[i],s[j] )
#        break

#for i in range(len(s)):
#    for j in range(i+1, len(s)):
#        if s[i] == s[j]:
#            print(i,j,"    ",s[i],s[j] )
#            i=len(s)
#            break
#    else:
#        continue
#    break
i=0
while i<10:
    print("i =",i)
    if i == 15:
        break
    i+=1
else:
    print("Cikl zavershilsya normalno")

        
        
        
            