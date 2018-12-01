from decimal import * 

def main():
    
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values
    aList = [1,1,9,25,49,81,121,169,225,289,361,441,529] #General cf: a list
    bList = [3,6,6,6,6,6,6,6,6,6,6,6] #General cf: b list
        
    for n in range(0,12):
        hList.append((Decimal(bList[n])*Decimal(hList[n+1])+Decimal(aList[n])*Decimal(hList[n])))
        kList.append((Decimal(bList[n])*Decimal(kList[n+1])+Decimal(aList[n])*Decimal(kList[n])))
        print ((Decimal(hList[n+2])/Decimal(kList[n+2])))
    
    print (hList)
    print (kList)
    
#call to main
main()
