#!/usr/bin/python3

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
