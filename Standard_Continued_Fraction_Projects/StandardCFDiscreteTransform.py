import math
import requests 
from decimal import *
import matplotlib
import matplotlib.pyplot as plt
 
def newRange(samples):
    newRange = []
    for i in range(0,samples):
        newRange.append(i*(2*math.pi)/samples)
    return newRange    

def CalcPowerSpectrum(x,y,z):
    yPower = []
    for j in range(0,len(y)):
        yPower.append(math.sqrt(math.pow(y[j],2)+math.pow(x[j],2)))
    plt.xlabel("Integer Frequency Test")
    plt.ylabel("Amplitude")
    plt.title("Discrete Fourier Transform")
    plt.bar(range(0,len(x)),yPower)
    plt.savefig("PowerSpectrumForZero" + str(z) + ".png")
    plt.clf()

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
        
    bList = [] # Stores the b values for the continued fraction
    for i in range(0,100):
        bList.append([])
        for n in range(0,30):
            bList[i].append(math.floor(b[i]))
            b[i] = 1/(b[i] - Decimal(b[i]).quantize(Decimal('1.'), rounding=ROUND_DOWN))
    
    for h in range(0,len(bList)):
        x = newRange(len(bList[h]))
        for k in range(0,len(bList[0])):
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
    
    
    
    #plt.clf()
    
    #for i in range(0,30):
        #temp = []
        #for j in range (0,100):
            #temp.append(bList[j][i])
        #plt.plot(temp)
    #plt.xlabel('the _ non-trivial zero (i.e. 1st, 2nd, 3rd ...)')
    #plt.ylabel('Value')
    #plt.title("Riemann Zeta Zero Standard CF Term Superposition (Zeroes 1-100)")
    #plt.ylim(top=200, bottom=0)
    #plt.savefig("RiemannZetaZeroesTerm" + "StandardCFPatternSuperpositionLimited" + ".png")
    
    plt.show()

    #f= open("LiebsSquareIceConstantStandardCF.txt","w+")
    #for i in range(0, 1000):
        #f.write(str(bList[i]))
        #f.write("\r\n")
    #f.close() 
    
    #plt.plot(bList)
    #plt.xlabel('term in the Standard Continued Fraction')
    #plt.ylabel('Value')
    #plt.title('Liebs Square Ice Constant Standard CF')
    #plt.show()
	
#call to main
main()
