#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Takes the data from a txt file (1000 digits of the first hundred zeta zeroes) and inputs this into a python list.
"""

from decimal import *
import requests 

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

def main():
    print(zetaZeroes())
    
main()