#!/usr/bin/env python3

import re
def integers_in_brackets(s):
    #[^[a-z ]\d+[^]]\b
    lista = re.findall(r'\[\s*[+-]?\d+\s*\]',s)
    uusilista = []
    for x in lista:
        sana = x.strip("[]+")
        sana2 = sana.strip()
        uusilista.append(int(sana2))
      
    return uusilista

def main():
    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!"""))

if __name__ == "__main__":
    main()
