"""
A universal cryptarithm-solver for adding up any number of terms.
Enter any cryptarithm to add any number of terms.
Input format: "TERMONE+TERMTWO+TERMTHREE=SUM"
By Romanko Vladimir, September 2019
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

"""                      MAIN PROGRAM    """

crypt = "TWO+TWO=FOUR"   # Enter any cryptarithm to add any number of terms.
# Input format: crypt = "TERMONE+TERMTWO+TERMTHREE=SUM"

###  PARSING OF crypt-string BEGIN
if crypt.count("=") != 1:
    print('PARSING ERROR: The number of characters "=" is not equal to one')
    raise SystemExit
crypt_lst=crypt.split("=");   print("crypt_lst =",crypt_lst)
if not crypt_lst[1].isalpha():
    print("PARSING ERROR: the SUM does not consist of letters")
    raise SystemExit
str3 = crypt_lst[1]
slag_lst = crypt_lst[0].split("+")
print("LIST OF TERMS =",slag_lst)
for sl in slag_lst:
    if not sl.isalpha():
        print("PARSING ERROR: one of the terms does not consist of letters")
        raise SystemExit
###  PARSING OF crypt-string END

lst_bukv=[];  str_lst=slag_lst.copy()
str_lst.append(str3)
for stroka in str_lst:
    for bukva in stroka:
        if bukva not in lst_bukv:
            lst_bukv.append(bukva)                       
l=len(lst_bukv)
#print("lst_bukv =", lst_bukv, "  l =",l )
print("Different leters =", lst_bukv)
print("Total amount of different letters =",l )
if l>10:
    print("THERE IS NO SOLUTION, because are more than 10 different letters")
    raise SystemExit
#print("slag_lst =", slag_lst,"   str_lst =", str_lst)
print("LIST OF WORDS =", str_lst)


slag_arr=foo(slag_lst, lst_bukv);   str3_arr=foo(str3, lst_bukv)
#print("slag_arr =", slag_arr);   print("str3_arr =", str3_arr)
slag_power=foo_power(slag_lst);   str3_power=foo_power([str3])
#print("slag_power =", slag_power);   print("str3_power =", str3_power)

resh=False
nach=1023456789;     konec=9876543210
NACH=nach // 10**(10-l);    KONEC=konec // 10**(10-l)
#print("NACH =", NACH, "KONEC =", KONEC)
np_lst_vspom = np.zeros(len(slag_arr), dtype=np.int32)
np_str3_vspom = np.zeros(len(str3_arr), dtype=np.int32)
t1=t.time(); #  print("t1-t0 =", t1-t0)

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
        for j in np.arange(len(slag_lst)):
            L=len(slag_lst[j])  
            for k in np.arange(L):
                print(I[lst_bukv.index(slag_lst[j][k])], end="") 
            if j != len(slag_lst)-1:
                print(" + ", end="")
#        print(" =",summ,"    I =",I)
        print(" =",summ,"    Different digits =",I)
    
if not resh:
    print("NO SOLUTION  FOUND")
t2=t.time();   print("Total program execution time is ", t2-t0, "seconds")
