# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:49:15 2024

@author: omidg
"""

qq = []#qq is the list that keeps the inputs with the highest number of prime divisors so far   
tool = 1#holds the length of prime divisors of the input numbers    
adad = 1
for i in range(0, 10):
    
    num = int(input())
    #maq contains all divisors of the input number
    maq = []
    for j in range(2, num):
        if num%j == 0:
            maq.append(j)
    #print(maq)
    #aval_maq contains the prime divisors of the input number    
    aval_maq = []
    for k in maq:
            for kk in range(2,k):
                if(k%kk == 0):
                    break
            else:
                aval_maq.append(k)
    #print(aval_maq)
    #print(len(aval_maq))
    
    if  len(aval_maq) >= tool:
        tool = len(aval_maq)
        qq.append(num)
        
print(max(qq), tool)