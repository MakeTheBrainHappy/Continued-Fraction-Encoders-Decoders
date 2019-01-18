import math 
from decimal import *
import matplotlib.pyplot as plt
 

def main():

    getcontext().prec = 1024
    value = open("RiemannZetaZeroes.txt","r")
    print value.read()
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
