#!/usr/bin/python3
print(sum([int(e) for e in list(bin(int(input("Enter N: ")))[2:]) if e]))
