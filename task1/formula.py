#!/usr/bin/python3

import math  # importing the whole thing


class Data:

    def __init__(self):
        try:
            self.a = float(input("Enter variable a: "))
            self.x = float(input("Enter variable x: "))
            self.beta = float(input("Enter variable beta: "))
        except ValueError:
            print("Error: please input only decimal numbers")
            exit(1)

        print("a: %s, x: %s, beta: %s" % (self.a, self.x, self.beta))


class Formula(Data):

    def calc(self):
        arcs = math.asin(self.x - 3 * self.beta)
        p2 = math.pow(self.a*math.pow(self.x, 3)+math.pow(math.e, self.a*self.x), 2)
        p3 = 0.3 * math.pow(10, -1.5) * self.x
        p4 = 1.3 * math.pow(10, 5) * math.fabs(self.x-math.pow(self.a, 5))  # fabs instead of abs because fabs is a part
        tg = math.tan(self.a + self.x)                                      # of math module and abs is not
        p5 = math.sqrt(math.pow(math.sin(self.a), 2) + math.pi)
        lg = math.log(self.x, 10)
        result = math.sqrt(math.fabs((arcs - p2 + p3) / (p4 - tg + p5 - lg)))
        print("result of calculations: ", result)


if __name__ == '__main__':
    formula = Formula()
    formula.calc()
