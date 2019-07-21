#!/usr/bin/env python3

class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.summa = a/b

    def suma(self):
        return self.summa

    def aa(self):
        return self.a

    def bb(self):
        return self.b

    def __str__(self):
        return str(self.a)+"/"+str(self.b)
    
    def __add__(self,luku):
        yla = (self.a*luku.bb()) + (luku.aa()*self.b)
        ala = self.b*luku.bb()
        #str(yla)+"/"+str(ala)
        return Rational(yla,ala)

    def __mul__(self,luku):
        yla = self.a*luku.aa()
        ala = self.b*luku.bb()
        return Rational(yla,ala)

    def __sub__(self,luku):
        yla = (self.a*luku.bb()) - (luku.aa()*self.b)
        ala = self.b*luku.bb()
        return Rational(yla,ala)

    def __truediv__(self,luku):
        ala = self.b*luku.aa()
        yla = self.a*luku.bb()
        return Rational(yla,ala)

    def __eq__(self,luku):
        if float(self.summa) == (luku.suma()):
            return True
        else:
            return False
    def __gt__(self,luku):
        if float(self.summa) > (luku.suma()):
            return True
        else:
            return False
    def __lt__(self,luku):
        if float(self.summa) < (luku.suma()):
            return True
        else:
            return False
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
