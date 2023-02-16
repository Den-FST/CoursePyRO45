# l0 = ["mar", 24, "Cireasa", 42, 0.5]
#
# l1 = []
# l2 = []
#
# for el in l0:
#     if type(el) is int:
#         print("{} este int".format(el))
#         l2.append(el)
#     elif type(el) is str:
#         print("{} este string".format(el))
#         l1.append(el)
#     else:
#         print("{} nu este nici int nici string".format(el))
#
# print(l1)
# print(l2)
#


"""
- trecem prin toate numerele de la 0 la 100
- la fiecare numar, verificam daca este impar (sa nu fie divizibil cu 2)
-  verificam daca e divizibil cu 3
- daca ambele conditii de mai sus sunt indeplinite, adaugam numarul respectiv la lista 'lista_0'
"""

# My variant
# lista_0 = []
# for n in range(0,100):
#     if not (n % 2 == 0) and (n % 3 == 0):
#         lista_0.append(n)
# print(lista_0)


# l1 = [True, 'Cirese', 'casa', 22, 0]
#
# while len(l1) > 2:
#     l1.pop()
#     print(l1)

lista1 = [1, 2, 3, 4, 70, 55, 7, 50, 9, 10]
lista2 = []
for x in lista1:
    if x < 20:
        lista2.append(x)
        set1 = set(lista1)
        set2 = set(lista2)
        lista1 = list(set1 - set2)

print(lista1)
print(lista2)