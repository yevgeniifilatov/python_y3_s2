#!/usr/bin/python3

from task4 import compare


def inputs():
    try:
        seq = int(input("Enter 0 for ascending, 1 for descending: "))
        if seq != 0 and seq != 1:
            print("Error: sequence input can be only 1 and 0")
            exit(1)
        arr = input("Enter array: ").split()
        arr = [int(e) for e in arr]
    except ValueError:
        print("Error: please input only float or int!")
        exit(1)
    return seq, arr


def upd_arr(arr, seq):
    res = [arr[i]+i for i in range(len(arr))] if compare(seq, arr) else arr
    print(res)


if __name__ == '__main__':
    seq, arr = inputs()
    upd_arr(arr, seq)
