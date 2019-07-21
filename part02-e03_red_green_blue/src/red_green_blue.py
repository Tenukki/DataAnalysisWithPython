#!/usr/bin/env python3

import re

def red_green_blue(filename="C:\\Users\\Santeri\\data-analysis-with-python-summer-2019\\hy-data-analysis-with-python-summer-2019\\part02-e03_red_green_blue\\src\\rgb.txt"):
    with open(filename,"r") as f:
        palautuslista = []
        lines = f.readlines()
        lines.pop(0)

        for line in lines:
            sanalist2 = re.findall("\w+",line)
            sana = sanalist2[0]+"\t"+sanalist2[1]+"\t"+sanalist2[2]+"\t"
            sanalist2.pop(0)
            sanalist2.pop(0)
            sanalist2.pop(0)
            sana += " ".join(sanalist2)
         
            palautuslista.append(sana)
    return palautuslista


def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
