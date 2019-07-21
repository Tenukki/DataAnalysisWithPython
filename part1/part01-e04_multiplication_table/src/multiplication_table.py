#!/usr/bin/env python3


def main():
    line = ""
    for i in range(1,11):
        for x in range(1,11):
            print('{:4d}'.format(i*x), end = "")
        print()

if __name__ == "__main__":
    main()
