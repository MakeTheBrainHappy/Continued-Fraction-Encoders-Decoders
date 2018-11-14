def main():
    
    hList = [0,1] # Initializing the h values
    kList = [1,0] # Initializing the k values
    
    bList = [10.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 20.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 20.0] # Example CF
    
    for n in range(0,19):
        hList.append(bList[n]*hList[n+1]+hList[n])
        kList.append(bList[n]*kList[n+1]+kList[n])
        print (hList[n+2]/kList[n+2])
    
    print (hList)
    print (kList)
    
#call to main
main()
