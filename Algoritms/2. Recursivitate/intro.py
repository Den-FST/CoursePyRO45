'''
Calculati factorialul numarului natural n
metoda recursiva: n! = n * (n-1)!, if n > 1 and 0! = 1
1 *2 * ... * n
'''

def factorial(n):
    if n != 0:
        res = 1
        for i in range(1, n+1):
            res *= i
        print(f"Factorial de {n}! = {res}")
#     # print("Numarul = 0")

# def factorial(n):
#     if n == 0:
#         return 1
#         # return print('Terminat')
#     else:
#         return n * factorial(n-1)

# name = 'Ricki'
#
# if name.startswith('R'):
#     print("test")



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
    if n == 0 :
        return 0
    elif n ==1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)

'''
calculati factorialul numarului natural 
'''
def iter_fibbonaci(n):
    pass

"""Calculati frecventa unui numar x intr-un array a"""
def numarare(a, x):
    pass



import timeit
if __name__ == '__main__':
    n = 5
    # print(factorial(5))
    print(fibbonaci(5))
    # print(timeit.timeit(stmt="fibbonaci(n)", setup="from __main__ import fibbonaci, n", number=10))
    # print(timeit.timeit(stmt="iter_fibbonaci(n)", setup="from __main__ import iter_fibbonaci, n", number=10))
