#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Creates a chart of the most frequent digits in the first thousand digits of the first hundred non-trivial Riemann Zeta Zeroes.
"""

from decimal import *
import requests 
import matplotlib.pyplot as plt


def zetaZeroes():
    getcontext().prec = 1024
    a = requests.get('http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros2').text.splitlines()
    b = []
    for i in a:
        if '.' in i:
            b.append(i.strip())
        elif len(b) > 0:
            b[-1] += i.strip()
    b = list(map(Decimal, b))
    return b;

def digitManipulation(data):
    valuesList = [0,0,0,0,0,0,0,0,0,0]
    for i in data:
        a = str(i)
        for j in range(0,len(a)):
            if (a[j]!="."): 
                valuesList[int(a[j])] = valuesList[int(a[j])] + 1
    print(valuesList)
    plt.plot(valuesList)
    plt.show()

def main():
    digitManipulation(zetaZeroes())
    
main()