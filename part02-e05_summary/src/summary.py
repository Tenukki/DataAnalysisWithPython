#!/usr/bin/env python3

import sys
import math

def summary(filename):
    with open(filename,"r") as f:
        lista = []
        for xx in f:
            try:
                x = float(xx)
                lista.append(x)
            except ValueError:
                continue
        lista = [ float(x) for x in lista ]
        avg = (sum(lista)/len(lista))
        summa = 0
        for x in lista:
            summa += (float(x)-avg)**2
        end = math.sqrt(summa/(len(lista)-1))
        
        return (sum(lista),avg,end)
def main():
    #print(summary("C:\\Users\\Santeri\\data-analysis-with-python-summer-2019\\hy-data-analysis-with-python-summer-2019\\part02-e05_summary\\src\\example.txt"))
    listasys = sys.argv[1:]
    #print(listasys)
    for x in listasys:
        sana = x
        a,b,c = summary(sana)
        printti = "File: "+x+" Sum: "+"{:.6f}".format(a)+" Average: "+"{:.6f}".format(b)+" Stddev: "+"{:.6f}".format(c)
        print(printti)
        
if __name__ == "__main__":
    main()
