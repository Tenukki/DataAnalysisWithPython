#!/usr/bin/env python3

def detect_ranges(L):
    
    newList = []
    start = 0
    for i in range(1,len(L)):
        if L[i] != L[i-1]+1:
            newList.append(L[i-1])
        else:
            
            
            
    return newList

def main():
    L = [1,5,3,4,5,6,8,10]
    sorted(L)
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

