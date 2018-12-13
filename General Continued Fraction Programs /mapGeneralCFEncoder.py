from decimal import * 
import time
import math
import numpy as np
import numba
from numba import jit
from itertools import product
from numpy.polynomial.polynomial import polyval

continuedFractions = {}
value = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603")

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
    
def encoder():
    start_time = time.time()
    getcontext().prec = 100
    GCFs = set(product([1,2,3,4],repeat=7))
    map(decoder,GCFs)
    
    tempList = sorted(continuedFractions)
    tempVar = tempList[:15]
    for i in range(0,15):
        print("change in x: ", tempVar[i], "CF ", continuedFractions.get(tempVar[i]))
    
    print("--- %s seconds ---" % (time.time() - start_time))            

    
def main():
    encoder()

#call to main
main()
