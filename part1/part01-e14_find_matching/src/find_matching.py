#!/usr/bin/env python3

def find_matching(L, pattern):
    returnList = []
    
    for x,i in enumerate(L):
        if pattern in L[x]:
            returnList.append(x)

    return returnList

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
