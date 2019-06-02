#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Description: Examines the polar forms of the non-trivial zeroes to find patterns. 
"""

from decimal import *
import requests 
import math
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
import scipy
import numpy as np

def main():
    
    getcontext().prec = 1024
    a = requests.get('http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros2').text.splitlines()
    b = []
    for i in a:
        if '.' in i:
            b.append(i.strip())
        elif len(b) > 0:
            b[-1] += i.strip()
    b = list(map(Decimal, b))
    for i in range(0,100): 
        l = (b[i]**2+Decimal(.5)**2).sqrt()
        b[i] = b[i]*(b[i]/Decimal(.5))
    plt.plot(b)
    #x = np.asarray(range(1,101))
    #y = np.asarray(map(float,b))
    #print(np.polyfit(x,y,3))
    #plt.plot(list(map(lambda x: -1.56759588e-02*x*x*x+8.08697931e+00*x*x+4.63602387e+02*x--3.05339448e+02,range(0,100))),color='red')
    plt.plot(list(map(lambda x: 5.71207156*x*x+560.02677693*x-1137.03214275,range(0,200))),color='green')
    #plt.plot(list(map(lambda x: 1136.94600471*x-10944.65901491,range(0,100))))
    plt.show()
    
main()