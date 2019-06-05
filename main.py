#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Description: Compilation of Code for the "Analysis of the Non-Trivial Riemann Zeta Zeroes"
"""

from decimal import *
import math
import requests 
import matplotlib.pyplot as plt
import scipy
import numpy as np

"""
Takes the data from a txt file (1000 digits of the first hundred zeta zeroes) and inputs this into a python list.
"""
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

"""
Creates a chart of the most frequent digits in a dataset
"""
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

"""
Description: Examines the polar forms of the non-trivial zeroes to find patterns
"""
def polarForms(b):
    for i in range(0,100): 
        l = (b[i]**2+Decimal(.5)**2).sqrt()
        b[i] = b[i]*(b[i]/Decimal(.5))
    plt.plot(b)
    #x = np.asarray(range(1,101))
    #y = np.asarray(map(float,b))
    #print(np.polyfit(x,y,3)) // Generate the different regressions (equations)
    #plt.plot(list(map(lambda x: -1.56759588e-02*x*x*x+8.08697931e+00*x*x+4.63602387e+02*x--3.05339448e+02,range(0,100))),color='red')
    #plt.plot(list(map(lambda x: 5.71207156*x*x+560.02677693*x-1137.03214275,range(0,200))),color='green')
    #plt.plot(list(map(lambda x: 1136.94600471*x-10944.65901491,range(0,100))))
    plt.show()

"""
Description: Write a new txt file with the terms of the constant
"""
def produceData(constantName,terms):
    f= open(str(constantName),"w+")
    for i in range(0, len(terms)):
        f.write(str(terms[i]))
        f.write("\r\n")
    f.close() 
   
"""
Description: Given two standard continued fractions, this method prints out places where the terms differ. This was used here to compare Standard CFs generated with Wolfram Mathematica to Standard CFs generated with my python algorithm since there was initally significant floating point round-off error.
"""
def comparingCFs(List1,List2):
    for i in range(0,1000):
        if (List1[i] != List2[i]):
            print("Place in CF: ",i," Number from Wolfram: ",List1[i]," Number from my Standard CF ",List2[i])
            
"""
Description: Generates standard continued fractions (30 terms) for each number in a given list of numbers
"""
def generateSCF(b):
    bList = [] # Stores the b values for the continued fraction
    for i in range(0,len(b)):
        bList.append([])
        for n in range(0,30):
            bList[i].append(math.floor(b[i]))
            b[i] = 1/(b[i] - Decimal(b[i]).quantize(Decimal('1.'), rounding=ROUND_DOWN))
    return(bList)

"""
Description: Plot standard continued fractions
"""
def plotSCF(constantName,terms): 
    plt.plot(terms)
    plt.xlabel('term in the Standard Continued Fraction')
    plt.ylabel('Value')
    plt.title(str(constantName) + " Standard CF")
    plt.show()

"""
Description: To plot this specific curve (https://github.com/MakeTheBrainHappy/Continued-Fraction-Encoders-Decoders/blob/master/Standard_Continued_Fraction_Projects/Patterns/RiemannZetaZeroesTermStandardCFPatternSuperposition.png and https://github.com/MakeTheBrainHappy/Continued-Fraction-Encoders-Decoders/blob/master/Standard_Continued_Fraction_Projects/Patterns/RiemannZetaZeroesTermStandardCFPatternSuperpositionLimited.png)
"""
def saveSuperpositionSCFPlot(bList):
    for i in range(0,30):
        temp = []
        for j in range (0,100):
            temp.append(bList[j][i])
    plt.plot(temp)
    plt.xlabel('the _ non-trivial zero (i.e. 1st, 2nd, 3rd ...)')
    plt.ylabel('Value')
    plt.title("Riemann Zeta Zero Standard CF Term Superposition (Zeroes 1-100)")
    plt.savefig("RiemannZetaZeroesTerm" + "StandardCFPatternSuperpositionLimited" + ".png")

"""
Description: Decodes standard continued fractions
"""
def decodeSCF(bList):
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values    
    getcontext().prec = 35
    for n in range(0,(len(bList)-2)):
        hList.append(Decimal(bList[n])*Decimal(hList[n+1])+Decimal(hList[n]))
        kList.append(Decimal(bList[n])*Decimal(kList[n+1])+Decimal(kList[n]))
    return Decimal(hList[n+2])/Decimal(kList[n+2])

"""
Description: Auxiliary function for the discrete fourier transform to change the domain of the data points.
"""
def newRange(samples):
    newRange = []
    for i in range(0,samples):
        newRange.append(i*(2*math.pi)/samples)
    return newRange

"""
Description: Power spectrum to show the dominant frequencies in graph form (a second auxiliary function for the DFT).
"""
def CalcPowerSpectrum(x,y,z):
    yPower = []
    for j in range(0,len(y)):
        yPower.append(math.sqrt(math.pow(y[j],2)+math.pow(x[j],2)))
    plt.xlabel("Integer Frequency Test")
    plt.ylabel("Amplitude")
    plt.title("Discrete Fourier Transform")
    plt.bar(range(0,len(x)),yPower)
    plt.savefig("PowerSpectrumForTerm" + str((z+1)) + ".png")
    #plt.plot()
    plt.clf()

"""
Description: Discrete Fourier Transform Code to rapidly do many SCFs (converts from time to frequency)
"""
def discreteFourierTransform(bList):
     for h in range(0,len(bList)):
        x = newRange(len(bList[h]))
        fSin = []
        fCos = []
        for i in range(0,len(bList[0])/2):
            fsin = 0
            fcos = 0
            for j in range(0,len(bList[0])):
                fsin+=(math.sin(i*x[j])*bList[h][j])
                fcos+=(math.cos(i*x[j])*bList[h][j])
            fsin/=len(bList[0])
            fcos/=len(bList[0])
            if (i>0):
                fsin*=2
                fcos*=2
            fSin.append(fsin)
            fCos.append(fcos)
        CalcPowerSpectrum(fSin,fCos,h)

"""
Description: Inverse Discrete Fourier Transform Code (converts from frequencies to time)
"""
def reconstructWave(samplesCount,x,fSin,fCos):
    y = []
    for i in x:
        yt=0
        for j in range(0,len(fCos)):
            yt += fSin[j]*math.sin(j*i)
            yt += fCos[j]*math.cos(j*i)
        y.append(yt)
    return y;

def main():
    #zetaZeroes() 
    #digitManipulation(zetaZeroes())
    #polarForms(zetaZeroes())
    #generateSCF(zetaZeroes())
    #decodeSCF(generateSCF(zetaZeroes()))
    #discreteFourierTransform(generateSCF(zetaZeroes()))
    x = generateSCF(zetaZeroes())
    discreteFourierTransform([[x[j][i] for j in range(len(x))] for i in range(len(x[0]))])
    
#call to main
main()    