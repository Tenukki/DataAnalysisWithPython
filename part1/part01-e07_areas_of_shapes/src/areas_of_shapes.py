#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = float(input("Give base of the triangle:"))
            height  = float(input("Give base of the triangle:"))
            print("The area is",base*height/2)
        elif shape == "rectangle":
            base = float(input("Give base of the triangle:"))
            height  = float(input("Give base of the triangle:"))
            print("The area is",base*height)
        elif shape == "circle":
            radius = float(input("Give radius of the circle:"))
            print("The area is",math.pi*radius**2)
        elif shape == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
