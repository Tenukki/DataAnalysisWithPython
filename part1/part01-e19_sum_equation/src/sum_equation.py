#!/usr/bin/env python3

def sum_equation(L):
    suma = str(sum(L))
    x = list(map(lambda a : str(a),L))
    if len(L) == 0:
        return "0 = 0"
    else:
        sana = " + ".join(x)
        return sana + " = " + suma

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
