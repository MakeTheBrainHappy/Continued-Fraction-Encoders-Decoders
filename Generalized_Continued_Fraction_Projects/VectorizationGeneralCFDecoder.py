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
 
    value = 67.079810529494173714478828896522216770107144951745558874196669551694901218956196983530293975085833034305554701005134859631029151896043171815867354023194548367379040086702914780981794419678446124381438361758449362432396595448051672339388685066004214583341246451635021345298388413847073026983988212589993826423870085245099897564429667355104289878620718854072588546515573973459707071676273108576334932180772579130003960886449741836868715353947764759128350375674332037097265984118710070440446053451664131052421556680265235785072265274438876785626696038697482052096822374418507817943850224433466786174237419767373787309963680688765295690311108804218807366754481244754126423472826840008964978766958987469469952222948151276077984728912688004788165878196172194802776783863053597521117816013422995841342604633581716447324616352745933784570730430336484481280084073724559292321162614130247542832542954781778971577652485927891091400797975856467160901917331051889540357656938483469207036091770874090798196914244237793474312960465161719018

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