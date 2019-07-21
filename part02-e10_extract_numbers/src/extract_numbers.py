#!/usr/bin/env python3

def extract_numbers(s):
    lista = s.split(" ")
    uusilista = []
    for x in lista:
        try: 
            uusilista.append(int(x))
        except:
            try:
                uusilista.append(float(x))
            except:
                pass
        
    return uusilista

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
