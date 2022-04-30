#!/usr/bin/python3

from math import sqrt  # import only sqrt from math - we don't need anything else


class Triangle:

    def __init__(self):
        try:
            self.sidea = int(input("Enter length of side a: "))  # here int type is used due to task using only integers
            self.sideb = int(input("Enter length of side b: "))  # can be easily changed to float if needed
            self.sidec = int(input("Enter length of side c: "))
        except ValueError:
            print("Error: please input only integers!")
            exit(1)

        self.test_triangle()

        print("Triangle has sides a: %i b: %i c: %i" % (self.sidea, self.sideb, self.sidec))

    def test_triangle(self):
        print(self.sidea + self.sideb)
        if self.sidea + self.sideb <= self.sidec \
                or self.sidec + self.sideb <= self.sidea \
                or self.sidea + self.sidec <= self.sideb:
            print("Error: triangle with these side lengths can't exist")
            exit(1)


class CalculateTriangle(Triangle):

    def area(self):  # here we don't use class variables because we don't need them anywhere else
        sp = (self.sidea + self.sideb + self.sidec) / 2  # half of perimeter - semi-perimeter
        tmp = sp * (sp - self.sidea) * (sp - self.sideb) * (sp - self.sidec)  # area squared
        area = sqrt(tmp)
        print(round(area, 4))  # rounding up to 4 decimals after dot, trailing zeroes will be collapsed


if __name__ == '__main__':
    test_tri = CalculateTriangle()
    test_tri.area()
