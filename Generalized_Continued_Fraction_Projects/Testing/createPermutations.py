#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Description: Creates a pre-generated list of permutations for use
"""

import pickle
from itertools import product

def main():
    GCF = list(product([-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10], repeat=5))
    constants = list(product([1,2,3,4,5,6,7,8,9,10],repeat=2))
    GCFs = []
    for i in constants:
        for j in GCF:
            GCFs.append(i + j)
    with open("test.txt", "wb") as fp:
        pickle.dump(GCFs, fp)

main()