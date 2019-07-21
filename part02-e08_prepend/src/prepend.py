#!/usr/bin/env python3

class Prepend(object):
    
    def __init__(self,sana):
        self.start = sana
    
    def write(self,xx):
        print(self.start+xx)
    # Add the methods of the class here
    

def main():
    x = Prepend("+++ ")
    x.write("Hello")

if __name__ == "__main__":
    main()
