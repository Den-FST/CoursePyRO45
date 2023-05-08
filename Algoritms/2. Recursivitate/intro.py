'''
Calculati factorialul numarului natural n
metoda recursiva: n! = n * (n-1)!, if n > 1 and 0! = 1
'''


def factorial(n):
    pass


'''
Calculati factorialul numarului natural n
metoda iterativa n! = n*(n-1)*...*1, if n > 1 and 0! = 1 
'''


def iter_factorial(n):
    pass


'''
Calculati al n-lea termen al seriei fibbonaci
metoda recursiva
'''


def fibbonaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonaci(n - 1) + fibbonaci(n - 2)

# (n-1)*(n-2)*3 = O(n^2) - time
# O(n) - spatiu
'''
calculati factorialul numarului natural 
'''


def iter_fibbonaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    old, new = 0, 1
    for i in range(n - 1):
        old, new = new, old + new
    return new


"""Calculati frecventa unui numar x intr-un array a"""

a = [5, 1, 2, 5, 6, 8, 4, 2, 5, 1, 0]


def numarare(x, i):
    if i == len(a):
        return 0
    if x == a[i]:
        return 1 + numarare(x, i + 1)
    else:
        return numarare(x, i + 1)


import timeit

if __name__ == '__main__':
    print(numarare(8, 0))
    # n = 20
    # print(timeit.timeit(stmt="fibbonaci(n)", setup="from __main__ import fibbonaci, n", number=10))
    # print(timeit.timeit(stmt="iter_fibbonaci(n)", setup="from __main__ import iter_fibbonaci, n", number=10))
