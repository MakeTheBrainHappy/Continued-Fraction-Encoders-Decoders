import time
import numpy as np
from numpy.polynomial.polynomial import polyval
from itertools import product
import math
import csv
from collections import OrderedDict
#import pickle
#import sys

continuedFractions  = {}

count = 0

def decoder(x):
    
    global continuedFractions
    
    global count
    
    batch_size = x.shape[0]
 
    value = 32.935061587739189690662368964074903488812715603517039009280003440784815608630551005938848496135348724549602525280597581513579237782857754506037653011472682109825272713659478166079186507881170353836765474601738548120651787886596466594728787186027971658042677648544066692909393193115645508391751300790279989562656683920024874165169990868845012876404250956064144893023774797053252782409947751765944607446809874067065338290958915614204800224198408375141584435237806584753908207901246070504560100102257438966836495384237704204909559898148908828725637297965721416526317785755201155077784057950147720725798214042130968637793635364185940239585699090026826663214819343540824642411198675065226034566669947805384925779001837592451461820738574360137810637371561037862089022277413320417734643423628639629736284445542467946705724129455369859667727596107799501092598501136571980327345054062391125982107996408750156764769596419463847304800451155728883660650892331803497715016444348320656123479340307063230555187773781024210561808202609296218

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

    
    if (len(continuedFractions) >= 512000):
        continuedFractions = OrderedDict(sorted(continuedFractions.items()))
        w = csv.writer(open("output" + str(count) + ".csv", "w"))
        for key, val in continuedFractions.items():
            w.writerow([key, val])
        continuedFractions  = {}
        count+=1
 
    return (continuedFractions)
  
def encoder():
    global continuedFractions
    start_time = time.time()
    #GCF = list(product([4,5,6,7,8,9,10], repeat=5))
    #constants = list(product([1,2,3,4,5,6,7,8,9,10],repeat=2))
    #GCFs = []
    #for i in constants:
        #for j in GCF:
            #GCFs.append(i + j)
            
    GCFs = list(j + i for i in product(range(-9, 11), repeat=5) for j in product(range(1, 11), repeat=2))
            
    #with open("test.txt", "rb") as fp:
        #GCFs = pickle.load(fp)
    
    #print(sys.getsizeof(GCFs))

    #-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,
        
    GCFs = np.array(GCFs)
        
    # Larger batches are faster
    # Larger batches use more memory
    print("--- %s seconds ---" % (time.time() - start_time))

    batch_size = 2500
    i = 0
    while i < len(GCFs):
        batch = GCFs[i:i+batch_size]
        decoder(batch)
        i += batch_size
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    continuedFractions = OrderedDict(sorted(continuedFractions.items()))

    w = csv.writer(open("output" + str(count) + ".csv", "w"))
    for key, val in continuedFractions.items():
        w.writerow([key, val])
    
    #print(sys.getsizeof(continuedFractions))

    #tempList = sorted(continuedFractions)
    #tempVar = tempList[:15]
    #for i in range(0, min(15, len(tempVar))):
        #print("change in x: ", tempVar[i], "CF ",
              #continuedFractions.get(tempVar[i]))
 
    print("--- %s seconds ---" % (time.time() - start_time))
 
def main():
    encoder()
 
# call to main
main()