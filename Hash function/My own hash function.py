'''  This program has created a hash function that converts
 any incoming message (string data type) into a hash (mishmash).
 The hash has a dimension of 256 bits and is a number in
 the hexadecimal number system. The resulting hash string
 always has two characters "0x" at the beginning and then 
 64 characters [0-9] and [a-f].
 
 For example, the message "Here is a statement" becomes this hash:
 "0xd44b94d9bc030cecc46d1ba51d103bf5885d2355222566a1dd3fb6f9fca97f63"

At the end of the program, the user can test this hash function.
 To do this, you need to enter two messages as the 
 variables message1 and message2. Then a hash function
 is taken from both messages. The counter then counts
 the number of matching characters in the two hashes. 
 If the number of matches is greater than four, then
 the hash function is of poor quality. If about four,
 then good quality.

By Vladimir Romanko, March 2023.       '''

import numpy as np
from itertools import permutations

'''       BIG HASH FUNCTION       '''
def HASH2(message):
    if message == '':
        message = 'asdf'
    dlina = len(message)
    ord_array = np.zeros(dlina, dtype = int)

    for i in np.arange( 0, dlina ):
        ord_array[i] = int( ord(message[i]) )
    mean = np.mean(ord_array)     
        
    var, asim, excess, slicee, mega_sum, sinn, ORD, decimal = 0,0,0,0,0,0,0,0
    vycypka = ''; kmax = 9  
    k = np.zeros(kmax, dtype = float)
    decimal = int('1')
    for i in np.arange(0, dlina):
        var += (ord_array[i] - mean)**2
        asim += (ord_array[i] - mean)**3
        excess += (ord_array[i] - mean)**4
        slicee += int( (1 + i) * ord_array[i] )
        if slicee > 10**12:
            slicee //= 100

    for i in np.arange(0, dlina):
        if i == dlina - 1:
            if i % 2 == 0:
                mega_sum += ord_array[0] & ord_array[i]
            else:
                mega_sum += ord_array[0] | ord_array[i]
            mega_sum += ord_array[0] * ord_array[i]
        else:
            if i % 2 == 0:
                mega_sum += ord_array[i+1] & ord_array[i]
            else:
                mega_sum += ord_array[i+1] | ord_array[i]
            mega_sum += ord_array[i+1] * ord_array[i]        
        if mega_sum > 10**11:
            mega_sum //= 100         
        
    if dlina > 60:
        predel = 60
    else:
        predel = dlina
    for i in np.arange(0, predel):
        binn = bin(ord_array[i])[2:]
        if (i > len(binn) - 1):
            index = i % len(binn)
            vycypka += binn[index]
        else:
            vycypka += binn[i]        
            
    var /= dlina
    asim /= dlina
    excess /= dlina
    if slicee > 10**12:
        slicee = np.sqrt(slicee)
    if asim > 10**12:
        asim = np.sqrt(asim)
    if var > 10**12:
        var = np.sqrt(var) 

    k[0] = mean * 10  
    k[1] = var   
    k[2] = abs(asim)  
    k[3] = np.sqrt(excess) * 100  
    k[4] = ( np.min(ord_array) + np.max(ord_array) ) * np.e * 10 
    k[5] = slicee 
    k[6] = int(vycypka,2)  
    k[7] = abs(mega_sum)  

    lst = [''.join(p) for p in permutations('1469')]
    for i in np.arange(0,kmax):
       if k[i] < 200:
           k[i] += int(lst[i])
       sinn += abs( np.sin(k[i]) )
       
    k[8] = sinn * 10000  
           
    for i in range(0, kmax):
        ORD += int(k[i]) * (1 + i)
        if i == kmax - 1:
            decimal += int(k[i]) * int(k[0])
        else:
            decimal += int(k[i]) * int(k[i+1])
        if decimal > 10**22:
            decimal //= 10000
            
    decimal += ORD
    bit256 = bin(decimal)[2:]
    i = kmax - 1
    while len( bin(decimal) ) < 258:
        decimal = decimal * int(k[i]) + int(k[i])
        i -= 1
        if i < 0:
            i += kmax
    bit256 = bin(decimal)[2:258]
    hashh = hex( int(bit256,2) )
    return hashh

'''            MAIN PROGRAM          '''

''' hash function quality check      '''
message1 = 'c' * 1002   ;   message2 = 'z' * 1003 
coincidence = 0
h1 = HASH2(message1); h2 = HASH2(message2)
print('h1 =',h1);   print('h2 =',h2)

for i in np.arange( 2,len(h1) ):
    if h1[i] == h2[i]:
        coincidence += 1
print('Number of matches (coincidence) in two hashes =', coincidence)


