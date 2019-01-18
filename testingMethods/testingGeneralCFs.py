import math 
from decimal import * 
import time
import numpy as np
import numba
from numba import jit

def decoder(a0,b0,a,b,c,d,e,value,continuedFractions):
    
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values
    aList = [1,Decimal(a0)] #General cf: a list
    bList = [Decimal(b0)] #General cf: b list
    
    for n in range(1,25):
        aList.append(Decimal(a)*Decimal(n)*Decimal(n)+Decimal(b)*n+Decimal(c))
        bList.append(Decimal(d)*Decimal(n)+Decimal(e))
        
    for n in range(0,24):
        hList.append((Decimal(bList[n])*Decimal(hList[n+1])+Decimal(aList[n])*Decimal(hList[n])))
        kList.append((Decimal(bList[n])*Decimal(kList[n+1])+Decimal(aList[n])*Decimal(kList[n])))
        
    temp = "a0 ",a0, "b0 ",b0, "a ",a, "b ",b,"c ",c,"d ",d,"e ",e 
    if (Decimal(kList[25] != 0)):
        continuedFractions[math.fabs(value-(Decimal(hList[25])/Decimal(kList[25])))] = temp
    return(continuedFractions)

@jit    
def encoder():
    start_time = time.time()
    value = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603")
    continuedFractions = {}
    decoder(1,3,2,4,4,2,4,value,continuedFractions)                                    
    
    tempList = sorted(continuedFractions)
    tempVar = tempList[:15]
    for i in range(0,1):
        print("change in x: ", tempVar[i], "CF ", continuedFractions.get(tempVar[i]))
    
    print("--- %s seconds ---" % (time.time() - start_time))            

    
def main():
    encoder()

#call to main
main()
