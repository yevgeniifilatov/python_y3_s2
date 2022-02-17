#!/usr/bin/python3

from math import sqrt, pow, e


def inputs():
    try:
        x = float(input("Enter x: "))
        a = float(input("Enter a: "))
    except ValueError:
        print("Error: please input only int or float!")
        exit(1)
    return x, a


def calc(x, a):
    res = a - a * pow(e, x-8*a) if x < 8*a else sqrt(2*a*x-16*a*a)
    print("Result: %f" % res)


if __name__ == '__main__':
    x, a = inputs()
    calc(x, a)
