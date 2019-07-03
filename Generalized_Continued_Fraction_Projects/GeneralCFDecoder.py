def main():
    
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values
    aList = [1,1,9,25,49,81,121,169,225,289,361,441,529,625,729] #General cf: a list
    bList = [3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6] #General cf: b list
        
    for n in range(0,15):
        hList.append((bList[n]*hList[n+1]+aList[n]*hList[n]) + 0.0)
        kList.append((bList[n]*kList[n+1]+aList[n]*kList[n] + 0.0))
        print ((hList[n+2]/kList[n+2]))
    
    print (hList)
    print (kList)
    
#call to main
main()
