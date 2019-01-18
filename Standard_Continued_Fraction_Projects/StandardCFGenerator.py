import math
import requests 
from decimal import *
import matplotlib.pyplot as plt
 

def main():
    
    import requests
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
    print(b)
    print(b[0])
    
    #zeroes = []
    #getcontext().prec = 1024
    #value = open("RiemannZetaZeroes.txt","r")
    #value = value.readlines()
    #print(value)
    #for i in range(0,len(value)):
        #value[i] = value[i].strip()
    #value = list(filter(None, value))
    #newList = []
    #newList.append("".join(value))
    #print newList
    
    #bList = [] # Stores the b values for the continued fraction
    #for n in range(0,1000):
        #bList.append(math.floor(value))
        #value = 1/(value - Decimal(value).quantize(Decimal('1.'), rounding=ROUND_DOWN))
    #print(bList)
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
