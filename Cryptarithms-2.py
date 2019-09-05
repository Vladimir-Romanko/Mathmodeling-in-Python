"""
CRYPTARITHMS 2   --   by wowik SEPTEMBER 2019  TUT ETO BRANCH1, NAH !!!
"""
import numpy as np
import itertools
import time as t
t0=t.time()

def diff_symb(chislo):
    st=""
    string = str(chislo)
    for symb in string:
        if symb not in st:
            st+=symb
        else:
            return False 
    return True
    
def generator(nachh,konecc):
    for z in range(nachh, konecc+1):
        if diff_symb(z):
            yield z

def foo(NUMB_LST, LST_BUKV):
    NUMB_ARR=[]
    for stroka in NUMB_LST:
        for char in stroka:
            NUMB_ARR.append(LST_BUKV.index(char))
    return np.array(NUMB_ARR)   

def foo_power(NUMB_LST):
    POWER_ARR=[]
    for stroka in NUMB_LST:
        lenn=len(stroka)
        for char in stroka:
            POWER_ARR.append(lenn-1)
            lenn-=1
    NP_POWER_ARR=np.array(POWER_ARR)
    ARR = 10**NP_POWER_ARR
    return ARR   

crypt = "BIT+COIN=BOOM" 
#slag_lst = ["AB","CDF","ABF"];     str3 = "FEBC"     # 6s iznachalno
#slag_lst=["AB","CD","ABC"];     str3="EBC"    # 1s iznachalno
#slag_lst=["TT","TT"];     str3="ABC"  
###  PARSING BEGIN
if crypt.count("=") != 1:
    print('PARSING ERROR: 4ISLO ZNAKOV "RAVNO" NE EDINICA')
    raise SystemExit
crypt_lst=crypt.split("=");   print("crypt_lst =",crypt_lst)
if not crypt_lst[1].isalpha():
    print("PARSING ERROR: SUMMA NE SOSTOIT IZ BUKV")
    raise SystemExit
str3 = crypt_lst[1]
slag_lst = crypt_lst[0].split("+");  print("slag_lst =",slag_lst)
for sl in slag_lst:
    if not sl.isalpha():
        print("PARSING ERROR: ODNO IZ SLAGAEMYH NE SOSTOIT IZ BUKV")
        raise SystemExit
### PARSING END

lst_bukv=[];  str_lst=slag_lst.copy()
str_lst.append(str3)
for stroka in str_lst:
    for bukva in stroka:
        if bukva not in lst_bukv:
            lst_bukv.append(bukva)                       
l=len(lst_bukv)
print("lst_bukv =", lst_bukv, "  l =",l );
if l>10:
    print("Resheniya ne suwestvuet, ibo raznyh bukv > 10")
    raise SystemExit
print("slag_lst =", slag_lst,"   str_lst =", str_lst)

slag_arr=foo(slag_lst, lst_bukv);   str3_arr=foo(str3, lst_bukv)
print("slag_arr =", slag_arr);   print("str3_arr =", str3_arr)
slag_power=foo_power(slag_lst);   str3_power=foo_power([str3])
print("slag_power =", slag_power);   print("str3_power =", str3_power)

resh=False
nach=1023456789;     konec=9876543210
NACH=nach // 10**(10-l);    KONEC=konec // 10**(10-l)
print("NACH =", NACH, "KONEC =", KONEC)
np_lst_vspom = np.zeros(len(slag_arr), dtype=np.int32)
np_str3_vspom = np.zeros(len(str3_arr), dtype=np.int32)
t1=t.time();   print("t1-t0 =", t1-t0)

#for i in range(NACH, KONEC+1): 
#for i in [c for c in range(NACH, KONEC+1) if diff_symb(c)]: 
for i in generator(NACH, KONEC): 
    I=str(i)
    cont=False
    for p in str_lst[1:]:
        x=int(I[lst_bukv.index(p[0])])
        if x==0:
            cont=True
            break
    if cont:
        continue

    for j in np.arange(len(slag_arr)):
        np_lst_vspom[j] = int(I[slag_arr[j]]) 
    slag_summ = sum(np_lst_vspom*slag_power)  

    for j in np.arange(len(str3_arr)):
        np_str3_vspom[j] = int(I[str3_arr[j]]) 
    summ = sum(np_str3_vspom*str3_power)    
    
    if slag_summ == summ:
        resh=True
#        print(slag[0], end=" ")
#        for sl in slag[1:]:
#            print("+",sl,end=" ")  
        for j in np.arange(len(slag_lst)):
            L=len(slag_lst[j])  
            for k in np.arange(L):
                print(I[lst_bukv.index(slag_lst[j][k])], end="") 
            if j != len(slag_lst)-1:
                print(" + ", end="")
        print(" =",summ,"    I =",I)
    

if not resh:
    print("RESHENIE NE NAIDENO")
t2=t.time();   print("t2-t0 =", t2-t0)





