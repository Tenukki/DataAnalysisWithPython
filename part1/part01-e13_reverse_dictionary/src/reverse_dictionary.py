#!/usr/bin/env python3

def reverse_dictionary(d):
    D = d
    a = {}

    for key, value in D.items():
        if len(D.get(key)) > 1:
            for sanat in D.get(key):
                a.update({sanat:[key]})
        else:
            if value[0] in a:
                x = a.get(value[0])
                x.append(key)
                a[value[0]] = x
            else:
                a.update({value[0]:[key]})
    return a

def main():

    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(d)
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
