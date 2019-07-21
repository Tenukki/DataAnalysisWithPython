#!/usr/bin/env python3

def distinct_characters(L):
    dic = {}
    for x in L:
        count = len(set(x))
        dic.update({x:count})
    return dic

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
