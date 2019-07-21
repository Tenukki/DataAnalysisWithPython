#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename,"r") as f:
        lista = f.readlines()
        dic = {}
        for x in lista:
            sanat = x.split()
            for sana in sanat:
                sana = sana.strip("""!"#$%&'()*,-./:;?@[]_""")
                dic.update({sana:0})
        for x in lista:
            sanat = x.split()
            for sana in sanat:
                sana = sana.strip("""!"#$%&'()*,-./:;?@[]_""")
                if sana in dic:
                    dic[sana] =  dic[sana] + 1
    return dic
def main():
    print(word_frequencies("C:\\Users\\Santeri\\data-analysis-with-python-summer-2019\\hy-data-analysis-with-python-summer-2019\\part02-e04_word_frequencies\\src\\alice.txt"))

if __name__ == "__main__":
    main()
