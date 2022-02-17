#!/usr/bin/python3

from random import randrange


class ListGen:

    def __init__(self):
        try:
            self.n = abs(int(input("Enter length of list N (10 will be added to user input): ")))
        except ValueError:
            print("Error: please input only integers!")
            exit(1)
        self.n += 10
        print("Total length of list: %i" % self.n)
        self.lst = []

    def gen_list(self):
        for i in range(self.n):
            self.lst.append(randrange(0, 100))  # creating array with random numbers from 0 to 100 for readability
        print(*self.lst)

    def swap(self):
        self.gen_list()
        self.lst[0], self.lst[-1] = self.lst[-1], self.lst[0]  # -1 index means last element of list
        print(*self.lst)


if __name__ == '__main__':
    inst = ListGen()
    inst.swap()
