#!/usr/bin/env python3
import re
#ota jäjestyksessä nuo tiedot ja sitten myöhemmin splittaaa saatu stringgi 

def file_listing(filename="C:\\Users\\Santeri\\data-analysis-with-python-summer-2019\\hy-data-analysis-with-python-summer-2019\\part02-e02_file_listing\\src\\listing.txt"):
    with open(filename, "r") as f:
        lista = f.readlines()
        uusilista = []
        tuplelist = []
        for line in lista:
            uusilista = []
            date = re.findall(r'\S*',line)
            for a in date:
                if a != "":
                    uusilista.append(a)
            a = int(uusilista[4])
            b = uusilista[5]
            aa = int(uusilista[6])
            c = uusilista[7].split(":")
            c1 = int(c[0])
            c2 = int(c[1])
            d = uusilista[8]
            tuplelist.append((a,b,aa,c1,c2,d))

        
        
    return tuplelist

def main():
    print(file_listing())
    #sana2 = "-rw-r--r-- 1 jttoivon hyad-all a 164519 Dec 28 17:59 basics.png"
    #[a-zA-Z]{3,4} \d{2,3} \d{2,3}:\d{2,3}
    
   
if __name__ == "__main__":
    main()
