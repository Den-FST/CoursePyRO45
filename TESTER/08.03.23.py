"""
https://peps.python.org/pep-0008/

"""

x = 4
y = 7


# if x == 4:
#     print(x ,y)
# if x == 4:print(x, y)
#
# x, y = y, x
#
# print(x ,y)

# if x == 4: print(x, y)
# else: x, y = y, x ; print(x,y)

# var_one = ''
# var_two = ''
# var_three = ''
# var_four = ''
# def long_function_name(var_one, var_two,
#                          var_three, var_four):
#     pass
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)
#
# foo1 = long_function_name(var_one, var_two,
#     var_three, var_four)

# try:
#     print(7/3)
#     raise  TypeError('Aceasta este o eroare')
# except ZeroDivisionError:
#     print('Nu se poate imparti la 0')
# except Exception as e:
#     print('Erroare')
# finally:
#     print('A fost incercata impartirea la 0')


"""
Dictionarul este structura de date neordonata, modificabila si indexabila.
Dictionarul permite stocarea in cheie - valoare.
    - Cheile pot fi orice structura de date imutabila(str, int)
    
"""

dictionar_gol = {}
dictionar_gol = dict()

dictionar = {'chaie1' : 'valoare',
             'cheie2' : 'valoarea2',
             'cheie3' : 3,
             'cheie4' : [1, 2, 3],
             'cheie5' : {1: 'unu', 'cheie_sec2' : 2}
             }

list1 = ['mar', 'par', 'cires']
list1[1]
list1[0]
# print(dictionar['cheie5'][1])
# print(dictionar.get('cheie3'))

# print(dictionar.items())
# print(dictionar)
# Despachetarea

val1 , val2, val3, _ = (1, 2, 3, 4)

dictionar_secundar = {}

for k, v in dictionar.items():
    if isinstance(v, (int, str)):
        dictionar_secundar[v] = k

# print(dictionar_secundar)
#
# print(len(dictionar_secundar))

fructe = {
    'banane'    : 5,
    'mere'      : 3,
    'lamai'     : 2,
    'portocale' : 11
}

numar_portocale = fructe.pop('portocale')

# print(numar_portocale)

# print(fructe)

"""
Dictionarul este structura de date neordonata, modificabila si indexabila.
Dictionarul permite stocarea in cheie valoare
 - Cheile pot fi orice structura de date imutabila(str, int)

"""
from typing import Type

dictionar_gol = {}
dictionar_gol2 = dict()

dictionar = {
    "cheie1": "valoare1",
    "cheie2": "valoare2",
    "cheie3": 3,
    "cheie4": [1, 2, 3],
    "cheie5": {1: "unu", 2: "doi"}
}

# print(dictionar["cheie5"][1])
# print(dictionar["cheie6"])
# print(dictionar.get("cheie6", "Cheie Default"))

del dictionar["cheie3"]

# print(dictionar)

dictionar["cheie3"] = "Cheie Noua"

# print(dictionar)
#
# print(dictionar.items())

# Despachetarea
val1, _, _ = (1, 2, 3)

# print(val1)
dictionar_secundar = {}

for k, v in dictionar.items():
    if isinstance(v, (int, str)):
        dictionar_secundar[v] = k

# print(dictionar_secundar)

# lungimea unui dictionar
# print(len(dictionar_secundar))


fructe = {
    "banane": 5,
    "mere": 3,
    "lamai": 2,
    "portocale": 11
}

numar_portocale = fructe.pop("portocale")


# print(numar_portocale)
# print(fructe)

variabila = 1


class Bani:
    descriere = "Banii sunt folositi ca mijloc de schimb."
    def __init__(self, nume):
        self.nume = nume

    def __str__(self):
        return f"Acestia sunt {self.nume}"


class Bancnote(Bani):
    def __init__(self, nume, material):
        super().__init__(nume)
        self.material = material

    def __str__(self):
        return f"Acestia sunt bancnote de {self.nume}"


moneda1 = Bancnote("50 de bani", "metal")
moneda2 = Bancnote("10 bani", "metal")

print(moneda1.nume, moneda1.descriere)
print(moneda2.nume, moneda2.descriere)

bancnota1 = Bancnote("10 lei", "hartie")
bancnota2 = Bancnote("50 lei", "hartie")

# print(bancnota1.nume, bancnota1.material)
# print(bancnota2.nume, bancnota2.material)


class Moneda(Bani):
    def __init__(self, nume, material, valoare):
        super().__init__(nume)
        self.material = material
        self.valoare = valoare

    def __eq__(self, obj_moneda):
        return self.valoare == obj_moneda.valoare

    def __gt__(self, other):
        return self.valoare > other.valoare

    def __lt__(self, other):
        return self.valoare < other.valoare


moneda3 = Moneda("5 bani", "metal", 0.05)
moneda4 = Moneda("1 ban", "metal", 0.01)
moneda5 = Moneda("1 ban", "metal", 0.01)


print(moneda3.nume, moneda3.material, moneda3.descriere)
print(moneda4.nume, moneda4.material, moneda4.descriere)

print(moneda4)
print(bancnota2)

print(moneda4 == moneda3)
print(moneda3 > moneda4)
print(moneda3 < moneda4)



