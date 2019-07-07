#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
New Strategy
"""

import math
import requests 
from decimal import *
import matplotlib
import matplotlib.pyplot as plt

def decoder(bList,value):
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values
    aList = [value]*len(bList) #General cf: a list
    bList = bList #General cf: b list
        
    for n in range(0,90):
        hList.append((bList[n]*hList[n+1]+aList[n]*hList[n]) + 0.0)
        kList.append((bList[n]*kList[n+1]+aList[n]*kList[n] + 0.0))
        print (value*(hList[n+2]/kList[n+2]))

#def encoder(): 


def main():
    '''
    getcontext().prec = 1024
    a = requests.get('http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros2').text.splitlines()
    b = []
    for i in a:
        if '.' in i:
            b.append(i.strip())
        elif len(b) > 0:
            b[-1] += i.strip()
    b = list(map(Decimal, b))
    '''
    
    b = []
    
    pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535
    
    value = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535 
    
    b.append(math.floor(value))
    
    for i in range(0,100):
        value = pi/(value - b[i])
        b.append(math.floor(value))
    
    print(b)
    decoder(b,pi)
    
    #for i in range(0,30):
        #temp = []
        #for j in range (0,100):
            #temp.append(bList[j][i])
        #plt.plot(temp)
    #plt.xlabel('the _ non-trivial zero (i.e. 1st, 2nd, 3rd ...)')
    #plt.ylabel('Value')
    #plt.title("Riemann Zeta Zero Standard CF Term Superposition (Zeroes 1-100)")
    #plt.ylim(top=200, bottom=0)
    #plt.savefig("RiemannZetaZeroesTerm" + "StandardCFPatternSuperpositionLimited" + ".png")
    
    #plt.show()

    #f= open("LiebsSquareIceConstantStandardCF.txt","w+")
    #for i in range(0, 1000):
        #f.write(str(bList[i]))
        #f.write("\r\n")
    #f.close() 
    
    #plt.plot(bList)
    #plt.xlabel('term in the Standard Continued Fraction')
    #plt.ylabel('Value')
    #plt.title('Liebs Square Ice Constant Standard CF')
    #plt.show()

	
#call to main
main()