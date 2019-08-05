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
 
    value = 77.144840068874805372682664856304637015796032449234461041765231453151139164253715089408288694699737759759056874412689862739401015043448714791318685067209262509692449500569598542876993525949529386655515907890732199648947712250820352478570207374012914861152103578929079678094268718586402341944783860346706430810880909426809869882058457679190768712226687326836014675913906597219780274184138815734306541730015512005219415994953054177649034287070792970549518522178103669138493110400289908763125838747967104934425409045729053716238542894539734697938404467517845653982842873996850493681944191593492637849172325367363215884466442942711922492108245169377647915815628834469485346686315856231243295323609538238676146113601842703432707855722562393513833974296170905761529531226860673673497802362080120843068941880544294812645599285786304342142860013808561146024088198620632042297490278719397603494739334898514673824383470963996162236863904616161107577611336626543223117952517771125313274971976990352450981517833496024699864255959028093118

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