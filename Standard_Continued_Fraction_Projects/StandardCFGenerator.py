import math
import requests 
from decimal import *
import matplotlib.pyplot as plt
 

def main():
    
    getcontext().prec = 1024
    a = requests.get('http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros2').text.splitlines()
    b = []
    for i in a:
        if not i.strip():
            continue
        if '.' in i:
            b.append(i.strip())
    else:
        b[-1] += i.strip()
    b = list(map(Decimal, b))
    
    bList = [] # Stores the b values for the continued fraction
    for i in range(0,100):
        bList.append([])
        for n in range(0,30):
            bList[i].append(math.floor(b[i]))
            b[i] = 1/(b[i] - Decimal(b[i]).quantize(Decimal('1.'), rounding=ROUND_DOWN))
    
    for i in range(0,100):
        plt.plot(bList[i])
        plt.xlabel('term in the Standard Continued Fraction')
        plt.ylabel('Value')
        plt.title(str(i+1) + '- Riemann Zeta Zero Standard CF')
        plt.show()
        plt.savefig("RiemannZetaZero" + str(i+1) + "Standard CF" + ".png")
    
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
