# Functii
from math import sqrt
import time
import timeit
"""
1) input
2) realizeaza o procesare de date, analiza, face ceva
3) output
"""

#definitia
# def f1(): #semnatura
#     print('Buna ziua') # body, corp
#
# #calling the function
# #apelarea functiei
#
# f1()

# import time
#
# def ora():
#     print(time.ctime())
# ora()


# def patrat(x):
#     x = x**2
#     print(x)
# calcul = patrat(4)


# def salut(nume):
#     print("salut {}" .format(nume))
# salut("tudor")

# def aduna_2_numere(a, b):
#     s = a + b
#     #print(s)
#     return s
#
# rez = aduna_2_numere(3,9)
# print(rez)

# def radical(x):
#     math.sqrt(x)
#     return x
# y = int(input())
# rezultat = print(radical(y))



# def nume_prenume(nume, prenume):
#     nume_complet = nume + ' ' +prenume
#     return nume_complet
#
# x = str(input())
# y = str(input())
#
# persoana = nume_prenume(x, y)
# print(persoana)



# lista = []
# l2 = []
# def lista_check(l1, nr):
#     for n in l1:
#         if n < nr:
#             l2.append(n)
#     return l2
#
# # lista  = [x for x in range(0, 5)] # list compression
#
# for x in range(0,5):
#     inp = int(input())
#     lista.append(inp)
#
# check = lista_check(lista, 10)
# print(check)

# timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

# t1 = (22,43,3,23,6)
# lista = []
# def inm_2():
#     for n in t1:
#         lista = [x * 2 for x in t1]
#         # n = n * 2
#         # lista.append(n)
#     return lista
#
# rezultat = inm_2()
# print(rezultat)
#
#
#same with compression
# t1 = (22,43,3,23,6)
#
# def inm_2():
#     for n in t1:
#         lista = [x * 2 for x in t1]
#     return lista
#
# rezultat = inm_2()
# print(rezultat)

# def suma(*a):
#     sum = 0
#     for n in a:
#         sum += n
#     print(sum)
#
# suma(1,2,3,4)

# def afiseaza_toti_oamenii(*persoana):
#     for nume_mic in persoana:
#         print(nume_mic)
# afiseaza_toti_oamenii('Costel', 'Ion', 'Adrian')


# def anunta_evenimente(*zile):
#     s=''
#     for program_ore in zile:
#         program_ore_f = str(program_ore)
#         s += program_ore_f + ' '
#     print(s)
# anunta_evenimente("luni","marti","miercuri")


# def sum2(a, b):
#     return a+b
#
# # print( sum2(2,5) )
#
# def operatie(a, b, c):
#     return sum2(a, b) * c
#
# r = operatie(2, 4, 10)
# # print(r)


# def radical(n):
#     return sqrt(n)
#
# def delta(a,b,c):
#     return (b**2)-(4*a*c)
#
# def radacini_binominale(a,b,c):
#     dlt = delta(a, b, c)
#     radacini2 = (radical(dlt) - b) / (2 * a)
#     return radacini2
#
# print( radacini_binominale(2, 2, 4) )