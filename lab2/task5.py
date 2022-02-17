#!/usr/bin/python3

class Factorial:

    def __init__(self):
        try:
            self.n = int(input("Enter N: "))
            if self.n <= -4:
                print("Cannot calculate negative factorial")
                exit(1)
        except ValueError:
            print("Error: please input only integers!")
            exit(1)
        self.n += 5
        print("Calculating: %i!" % self.n)

    def calc(self):
        lst = [str(e) for e in list(range(1, self.n+1))]
        exp = '*'.join(lst)
        res = eval(exp)
        print("%i! is equal to\n%s\nResult: %i" % (self.n, exp, res))


if __name__ == '__main__':
    fact = Factorial()
    fact.calc()
