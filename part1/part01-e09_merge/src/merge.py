#!/usr/bin/env python3

def merge(L1, L2):
    l1 = L1
    l2 = L2

    x = l1+l2
    uusi = []
    
    for i in range(len(x)):
        smallest = min(x)
        uusi.append(smallest)
        x.remove(smallest)
 
    return uusi

def main():
    a = [1,2,3,4,6,7,7,8,0]
    b = [4,6,7,8,3,2]
    
    print(merge(a,b))
    

if __name__ == "__main__":
    main()
