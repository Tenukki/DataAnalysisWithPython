#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    x=math.sqrt((b**2)-(4*a*c))
    #print(x)
    xx=-b
    print(xx)
    aa = (xx + x)/(2*a)
    bb = (xx - x)/(2*a)
    return (aa,bb)

def main():
    print(solve_quadratic(-2,2,1))

if __name__ == "__main__":
    main()
