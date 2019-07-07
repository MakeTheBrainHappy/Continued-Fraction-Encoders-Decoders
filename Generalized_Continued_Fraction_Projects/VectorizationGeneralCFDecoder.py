import time
import numpy as np
from numpy.polynomial.polynomial import polyval
from itertools import product
import math
<<<<<<< HEAD
import csv
#import pickle
#import sys

=======
>>>>>>> parent of 6ca01b5... Uploaded some data
 
continuedFractions  = {}

def decoder(x):
    batch_size = x.shape[0]
 
<<<<<<< HEAD
    value = 21.022039638771554992628479593896902777334340524902781754629520403587598586068890799713658514180151419533725473642475891383865068603731321262118821624375741669256544711844071194031306725646227792614887337435552059147397132822662470789076753814440726466841906077127569834054514028439923222536788268236111289270057585653273158866604214000907115108009006972002799871101758475196322164968659005748112479386916383518372342780734490239101038504575641215958399921001621834669113158721748057170315793581797724963272407699221125663441561823605180476714422714655559673781247765004555840908644291697757046381655177496445249876742370366456577704837992029270664315837893238009151146858070430828784147861992007607760477484140782738907003895760433245127827863720909303797251823709180804230666738343799022825158287887617612661871382967858745623765006662420780814517636976391374340593412797549697276850306200263121273830462939302565414382374433344022024800453343883072838731260230654753483786801182789317520010690056016544152811050970637593228

=======
    value = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603
>>>>>>> parent of 6ca01b5... Uploaded some data
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
        #if(hList.shape[1] > 1):
            #if (math.fabs(hList[n+2]/kList[n+2]-value) > math.fabs(hList[n+1]/kList[n+1]-value)):
                
        
    # Look at each CF, possibly add it to continuedFractions
    for i in range(batch_size):
        temp = "a0 ", x[i,0], "b0 ", x[i,1], "a ", x[i,4], "b ", x[i,3], "c ",\
               x[i,2], "d ", x[i,6], "e ", x[i,5]
        if (kList[i,25] != 0):
            continuedFractions[
                math.fabs(value - (hList[i,25] / kList[i,25]))] = temp
<<<<<<< HEAD

    
    if (len(continuedFractions) >= 512000):
        continuedFractions = sorted(continuedFractions)
        w = csv.writer(open("output" + str(count) + ".csv", "w"))
        for key, val in continuedFractions.items():
            w.writerow([key, val])
        continuedFractions  = {}
        count+=1
=======
>>>>>>> parent of 6ca01b5... Uploaded some data
 
    return (continuedFractions)
  
def encoder():
    start_time = time.time()
<<<<<<< HEAD
    GCF = list(product([-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10], repeat=5))
    constants = list(product([1,2,3,4,5,6,7,8,9,10],repeat=2))
    GCFs = []
    for i in constants:
        for j in GCF:
            GCFs.append(i + j)
            
    #with open("test.txt", "rb") as fp:
        #GCFs = pickle.load(fp)
    
    #print(sys.getsizeof(GCFs))

    #-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,
        
    GCFs = np.array(GCFs)
        
=======
    GCFs = np.array(list(product([1,1,1,1,1,1,1], repeat=7)))
>>>>>>> parent of 6ca01b5... Uploaded some data
    # Larger batches are faster
    # Larger batches use more memory
    print("--- %s seconds ---" % (time.time() - start_time))

    batch_size = 2000
    i = 0
    while i < len(GCFs):
        batch = GCFs[i:i+batch_size]
        decoder(batch)
        i += batch_size
    
    print("--- %s seconds ---" % (time.time() - start_time))
<<<<<<< HEAD
    
    continuedFractions = sorted(continuedFractions)

    w = csv.writer(open("output" + str(count) + ".csv", "w"))
    for key, val in continuedFractions.items():
        w.writerow([key, val])
    
    #print(sys.getsizeof(continuedFractions))
=======
>>>>>>> parent of 6ca01b5... Uploaded some data

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