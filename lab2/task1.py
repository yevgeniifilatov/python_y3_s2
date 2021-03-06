
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

string = "Програміст — фахівець, що займається програмуванням, виконує розробку програмного забезпечення " \
         "(в простіших випадках — окремих програм) для програмованих пристроїв, які, " \
         "як правило містять один процесор чи більше"


def inputs():
    try:
        n = int(input("Enter N: "))
        if n > 25 or n <= -25:
            n = n % 25
    except ValueError:
        print("Error: please input only integers!")
        exit(1)
    tmp = 20 - n if n > 0 else (20-n) % 25
    return n, tmp


def swap_words(first, second):
    lst = string.split()
    first += 1 if not lst[first].isalpha() else 0
    second += 1 if not lst[second].isalpha() else 0
    lst[first], lst[second] = lst[second], lst[first]
    return ' '.join(lst)


if __name__ == '__main__':
    fst, scd = inputs()
    string_new = swap_words(fst, scd)
    print("before:\n%s\nAfter:\n%s" % (string, string_new))

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
