#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:10:00 2019

@author: theo
"""

import time
from sympy.utilities.iterables import multiset_permutations
from itertools import permutations
import numpy as np

global continuedFractions

def decoder(x):
    
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values
    aList = [1,x[0]] #General cf: a list
    bList = [x[1]] #General cf: b list
    temp = ""
    
    for n in range(1,25):
        aList.append(polyval(n, [x[4],x[3],x[2]]))
        bList.append(polyval(n, [x[6],x[5]]))
        
    for n in range(0,24):
        hList.append(bList[n]*hList[n+1]+aList[n]*hList[n])
        kList.append(bList[n]*kList[n+1]+aList[n]*kList[n])
        
    temp = "a0 ", x[0], "b0 ",x[1], "a ",x[2], "b ",x[3],"c ",x[4],"d ",x[5],"e ",x[6]
    if (kList[25] != 0):
        continuedFractions[math.fabs(value-Decimal(hList[25])/Decimal(kList[25]))] = temp
    return(continuedFractions)

def GCFTester():
    start_time = time.time()
    GCFs = multiset_permutations(np.array([0, 1, 2, 3, 4, 5, 6]))
    #for p in GCFs:
        #decoder(p)
    
    print("--- %s seconds ---" % (time.time() - start_time))

def main():
    GCFTester()
    
main()