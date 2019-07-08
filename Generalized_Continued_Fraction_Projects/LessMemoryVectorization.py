#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Description: Vectorization with the GCF Encoder but crafted to take up less memory
"""

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
 
    value = 37.586178158825671257217763480705332821405597350830793218333001113622149089618537264730329104945823803474577747746192235379940965022263936285624822047483688089003667890354537553777903190905644099375838721275634312643051507490897122077467801551204327992986651432331546548850586795060341362549259966882096153281156037995262203235784878311073776146230149105579379015677163411251265371295650176744886452149832702011984494315326208033153177607464795075040560820830213633950862288220551335769555803593746481598709080074079627217716472274070573805968351484679530321727608711240067379431833670679071307878785388574357730695112597437885627621434891374075997674405555785944574435456054998502810248039697965044333212466041270340603151340824120398066920929558272133080574742240379526941447560387171391417722823862277333504075259600092839740678450396055572399332457099842085439308578390827058000428133328048210695855943079835422972275055349593563168097527417304301276517837886885878256674412456445093066944548079936612500679148846677611635

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

def runBatches(GCFs,start_time):
    
    global continuedFractions
    
    global count
    
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
    count +=1 

def encoder():
    
    global continuedFractions
    
    start_time = time.time()
    GCF = list(product([-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10], repeat=5))
    constants = list(product([1,2,3,4,5,6,7,8,9,10],repeat=2))
    GCFs = []
    counts = 0
    for i in constants:
        for j in GCF:
            GCFs.append(i + j)
        counts += 1
        if ((counts)%(10)==0):
            runBatches(np.array(GCFs),start_time)
            GCFs = []
            
    #GCFs = list(j + i for i in product(range(-9, 11), repeat=5) for j in product(range(1, 11), repeat=2))
            
    #with open("test.txt", "rb") as fp:
        #GCFs = pickle.load(fp)
    
    #print(sys.getsizeof(GCFs))

    #-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,
        
    # Larger batches are faster
    # Larger batches use more memory
    #print("--- %s seconds ---" % (time.time() - start_time))

    #batch_size = 2500
    #i = 0
    #while i < len(GCFs):
        #batch = GCFs[i:i+batch_size]
        #decoder(batch)
        #i += batch_size
    
    #print("--- %s seconds ---" % (time.time() - start_time))
    
    #continuedFractions = OrderedDict(sorted(continuedFractions.items()))

    #w = csv.writer(open("output" + str(count) + ".csv", "w"))
    #for key, val in continuedFractions.items():
        #w.writerow([key, val])
    
    #print(sys.getsizeof(continuedFractions))

    #tempList = sorted(continuedFractions)
    #tempVar = tempList[:15]
    #for i in range(0, min(15, len(tempVar))):
        #print("change in x: ", tempVar[i], "CF ",
              #continuedFractions.get(tempVar[i]))
 
    #print("--- %s seconds ---" % (time.time() - start_time))
 
def main():
    encoder()
 
# call to main
main()