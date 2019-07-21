#!/usr/bin/env python3

def main():
    L = [(a,b) for a in range(1,7) for b in range(1,7) if a+b == 5]
    for a in L:
        print(a)

if __name__ == "__main__":
    main()
