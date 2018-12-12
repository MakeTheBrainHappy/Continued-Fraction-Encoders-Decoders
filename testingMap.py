def function(x):
    return (x[1]**2 + x[2]**2)

def main():
    print(map(function, ((1,2,3), (1,2,3))))
    
main()
