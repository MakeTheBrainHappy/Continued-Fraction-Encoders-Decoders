import time
import numpy as np
from numpy.polynomial.polynomial import polyval
from itertools import product
import math
 
continuedFractions  = {}
 
def decoder(x):
    global continuedFractions
    batch_size = x.shape[0]
 
    value = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603
    hList = np.array([[0, 1]]*batch_size)  # Initializing the h values
    kList = np.array([[1, 0]]*batch_size)  # Initializing the k values
    aList = x[:,0]
    aList = np.stack([np.ones_like(aList), aList], axis=1)
    bList = x[:,1:2]  # General cf: b list
 
    # Calculate a, b
    low_n = 1
    high_n = 25
    n = np.arange(low_n, high_n)
    new_a = polyval(n, x[:,2:5].transpose()) # Realign axis to match polyval's expectations
    new_b = polyval(n, x[:,5:7].transpose())
    aList = np.concatenate([aList, new_a], axis=1)
    bList = np.concatenate([bList, new_b], axis=1)
 
    # Calculate h, k for each n value
    for n in range(0, 24):
        new_h = (bList[:,n] * hList[:,n + 1] + aList[:,n] * hList[:,n])
        new_k = (bList[:,n] * kList[:,n + 1] + aList[:,n] * kList[:,n])
        new_h = np.expand_dims(new_h, axis=1)
        new_k = np.expand_dims(new_k, axis=1)
        hList = np.concatenate([hList, new_h], axis=1)
        kList = np.concatenate([kList, new_k], axis=1)
 
    # Look at each CF, possibly add it to continuedFractions
    for i in range(batch_size):
        temp = "a0 ", x[i,0], "b0 ", x[i,1], "a ", x[i,4], "b ", x[i,3], "c ",\
               x[i,2], "d ", x[i,6], "e ", x[i,5]
        if (kList[i,25] != 0):
            continuedFractions[
                math.fabs(value - (hList[i,25] / kList[i,25]))] = temp
 
    return (continuedFractions)
 
 
def encoder():
    start_time = time.time()
    GCFs = np.array(list(product([1, 2, 3, 4, 5, 6, 7], repeat=7)))
 
    # Larger batches are faster
    # Larger batches use more memory
    batch_size = 2000
    i = 0
    while i < len(GCFs):
        batch = GCFs[i:i+batch_size]
        decoder(batch)
        i += batch_size
 
    tempList = sorted(continuedFractions)
    tempVar = tempList[:15]
    for i in range(0, min(15, len(tempVar))):
        print("change in x: ", tempVar[i], "CF ",
              continuedFractions.get(tempVar[i]))
 
    print("--- %s seconds ---" % (time.time() - start_time))
 
 
def main():
    encoder()
 
# call to main
main()
