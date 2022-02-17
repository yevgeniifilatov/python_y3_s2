#!/usr/bin/python3

def ar_prog(a1, t, z):
    lst = [round(a1+t*i, 10) for i in range(z)]
    print(lst)
    res = eval('*'.join([str(e) for e in lst]))
    print("Result: %f" % res)


def inputs():
    try:
        a1, t, z = float(input("Enter a1: ")),  float(input("Enter t: ")), int(input("Enter z: "))
    except ValueError:
        print("Error: please input only float or int!")
        exit(1)
    return a1, t, z


if __name__ == '__main__':
    a1, t, z = inputs()
    ar_prog(a1, t, z)
