#!/usr/bin/env python3

def main():
   
    for i in range(1,7):
        for x in range(1,7):
            number = x+i
            if number == 5:
                print("(%i,%i)"%(i,x))
        

if __name__ == "__main__":
    main()
