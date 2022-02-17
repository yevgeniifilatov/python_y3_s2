#!/usr/bin/python3


def compare(seq, arr):
    res = True
    f = -1 if seq else 1
    for i in range(seq, len(arr)-1+seq):
        if not arr[i*f+f] > arr[i*f]:
            res = False
            break
    return res


def inputs():
    try:
        seq = int(input("Enter 0 for ascending, 1 for descending: "))
        n, arr = int(input("Enter N: ")) + 5, input("Enter array: ").split()
        if n != len(arr):
            print("Error: array length doesn't match N+5")
            exit(1)
        if seq != 0 and seq != 1:
            print("Error: sequence input can be only 1 and 0")
            exit(1)
        arr = [int(e) for e in arr]
    except ValueError:
        print("Error: please input only float or int!")
        exit(1)
    return seq, arr


if __name__ == '__main__':
    seq, arr = inputs()
    res = compare(seq, arr)
    print("Array is in order") if res else print("Array is not in order")
