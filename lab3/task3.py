#!/usr/bin/python3

def geo_prog(a1, t, alim):

    lst = []
    while a1 > alim:
        lst.append(round(a1, 10))
        a1 *= t
    print(lst)
    res = sum(lst)
    print("Result: %f" % res)


def inputs():
    try:
        a1, t, alim = float(input("Enter a1: ")),  float(input("Enter t: ")), float(input("Enter alim: "))
        if t < 0 or t > 1:
            print("Error: 0 < t < 1")
            exit(1)
    except ValueError:
        print("Error: please input only float or int!")
        exit(1)
    return a1, t, alim


if __name__ == '__main__':
    a1, t, alim = inputs()
    geo_prog(a1, t, alim)
