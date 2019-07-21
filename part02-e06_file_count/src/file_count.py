#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename,"r") as f:
        lista = f.readlines()
        linenumbers = len(lista)
        merkit = 0
        sanamaara = 0
        for lause in lista:
            merkit+=len(lause)
            sanat = lause.split()
            sanamaara += len(sanat)
        return (linenumbers,sanamaara,merkit)

def main():
    listasys = sys.argv[1:]
   # print(listasys)
    for x in listasys:
        sana = x
        a,b,c = file_count(sana)
        printti = str(a) +"\t"+ str(b) +"\t"+  str(c) +"\t"+ sana
        print(printti)
if __name__ == "__main__":
    main()
