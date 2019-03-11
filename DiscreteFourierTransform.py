#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Discrete Fourier Transform
"""

import matplotlib.pyplot as plt
import math

def newRange(samples):
    newRange = []
    for i in range(0,samples):
        newRange.append(i*(2*math.pi)/samples)
    return newRange

def makeSamples():
    xValues = []
    yValues = []
    samples = 100
    for x in newRange(samples):
        xValues.append(x)
        yValues.append(32*math.cos(2*x)+8*math.cos(15*x)+19*math.sin(10*x)+3*math.sin(34*x))
    return(xValues,yValues)

def CalcPowerSpectrum(x,y):
    yPower = []
    for j in range(0,len(y)):
        yPower.append(math.sqrt(math.pow(y[j],2)+math.pow(x[j],2)))
    plt.xlabel("Integer Frequency Test")
    plt.ylabel("Amplitude")
    plt.title("Discrete Fourier Transform")
    plt.bar(range(0,len(x)),yPower)
    #plt.savefig("PowerSpectrum.png")
    plt.show()

def main():
    lists = makeSamples()
    x = lists[0]
    y = lists[1]
    fSin = []
    fCos = []
    for i in range(0,len(x)/2):
        fsin = 0
        fcos = 0
        for j in range(0,len(x)):
            fsin+=(math.sin(i*x[j])*y[j])
            fcos+=(math.cos(i*x[j])*y[j])
        fsin/=len(x)
        fcos/=len(x)
        if (i>0):
            fsin*=2
            fcos*=2
        fSin.append(fsin)
        fCos.append(fcos)
    print(fSin)
    print(fCos)
    CalcPowerSpectrum(fSin,fCos)
    
main()