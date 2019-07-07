#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Purpose: Find the size in bytes of a dictionary of a certain size.
"""

import sys, itertools

def main():
    print(sys.getsizeof(dict(zip(range(320000000), itertools.cycle([1]))))) #https://stackoverflow.com/questions/45393694/size-of-a-dictionary-in-bytes/45393747
    
main()