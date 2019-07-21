#!/usr/bin/env python3


def triple(luku):
    return luku*3
def square(luku):
    return luku**2

def main():
    for x in range(1,11):
        s = square(x)
        t = triple(x)
        if s > t:
            break
        else:
            print("triple(%i)==%i square(%i)==%i" % (x,t,x,s))

if __name__ == "__main__":
    main()
