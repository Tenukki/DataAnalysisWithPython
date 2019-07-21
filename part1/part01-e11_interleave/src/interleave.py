#!/usr/bin/env python3

def interleave(*lists):
    newlist = []
    
    for x in zip(*lists):
        newlist.extend(x)
    return newlist

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
