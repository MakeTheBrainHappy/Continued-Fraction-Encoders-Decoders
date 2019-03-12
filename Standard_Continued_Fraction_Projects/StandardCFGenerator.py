import math
import requests 
from decimal import *
import matplotlib
import matplotlib.pyplot as plt
 

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
    
    for i in range(0,30):
        temp = []
        for j in range (0,100):
            temp.append(bList[j][i])
        plt.plot(temp)
    plt.xlabel('the _ non-trivial zero (i.e. 1st, 2nd, 3rd ...)')
    plt.ylabel('Value')
    plt.title("Riemann Zeta Zero Standard CF Term Superposition (Zeroes 1-100)")
    plt.ylim(top=200, bottom=0)
    plt.savefig("RiemannZetaZeroesTerm" + "StandardCFPatternSuperpositionLimited" + ".png")
    
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
