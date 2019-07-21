#!/usr/bin/env python3

def transform(s1, s2):
    aa = s1.split()
    s = s2.split()
    x = list(zip(aa,s))
    
    return list(map(lambda a,b : int(a)*int(b), aa,s))


def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
