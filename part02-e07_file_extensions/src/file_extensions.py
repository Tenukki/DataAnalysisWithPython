#!/usr/bin/env python3

import re

def file_extensions(filename):
    with open(filename,"r") as f:
        lista = f.readlines()
        
        dic = {}
        yks = []
        for sana in lista:
            word = re.findall(r"(\.\w+)$",sana) 
           # print(sana)
            if len(word) == 1:
                key = word[0].strip(".")
                if key not in dic:
                    l = []
                    l.append(sana.strip("\n"))
                    dic[key] = l
                else:
                    a = dic[key]
                    a.append(sana.strip("\n"))
                    dic[key] = a
            else:
                yks.append(sana)
        
       
       # print(yks)
       # print(dic)
        return(yks,dic)
        
def main():
    a, b = file_extensions("src/filenames.txt")
    if len(a) > 0:
        print(len(a),"files with no extension")
    else:
        print("0 files with no extension")
    for a,x in b.items():
        print(a,"",len(x))
if __name__ == "__main__":
    main()
