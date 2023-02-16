from decimal import Decimal
# 0-9m a-z, A-Z _

# Exemple de denumiri valide:

# 1) denumirea se face folosind caractere alfa-numerice, cifre si
# 2) primul caracter nu poate fi cifra
CLADIRE=0
masina=0
proprietate_numerica =0
Pisica23=0
_exemplu=0
# 23zona
# istoric

#int
x=1
y = 2


#float
z=0.4

s1 = "cuvint"
s2 = "alt_string"
s3 = "0 propozitie"
s4 = 't% $ - l$'


# print(type(s1))

d = 10 / 3

restul_impartirii = 10 % 3 #restul impartirii
catul_impartirii = 10 // 3 #catul impartirii

# print( type(restul_impartirii) )

e_soare_afara = True
nu_sunt_obosit = False


merg_la_piata = e_soare_afara or nu_sunt_obosit

# print(merg_la_piata)

P=3.14
R=15
# print((4 / 3)*P*(R**3))


l = 10
v = l ** 3
# print("Volumul cubului este:", v)
# print(v < 100)

a1 = 1
a2 = 2
b1 = 3
b2 = 4
cond1: bool = a1 < a2
cond2: bool = b1 < b2
# print(cond1 and cond2)

c1 = "Ovidiu"
c2 = "are"
c3 = "mare"

d = c1 + " " + c2 + " " +  c3

s1 = "La Multi Ani" * 10

# print(s1)
#
# print("-= ", d, " =-")

s2 = "Ana are " + "23" + "de mere"
numar_de_mere = 23
locatie_tara = "la tara"
s2 = "Ana are {} de mere {}".format(numar_de_mere, locatie_tara)

# print(s2)

s3 = "Ana are {1} de mere {0}".format(numar_de_mere, locatie_tara)

# print(s3)

s4 = "Ana are {x} de mere {y}".format(x=numar_de_mere, y=locatie_tara)

# print(s4)

s5 = f"Aceasta este o propozitie {numar_de_mere}"
# print(s5)

a=2
b=3
s6 = f"{a} inmultit cu {b} este {a*b}"
# print(s6)

x = 0.1234567
s7 = f"{x: .4f}"
# print(s7)

procente = 0.23

s8 = f"{procente: .1%}"
# print(s8)

# virsta , nume , ocupatie, locatie

virsta = 35
nume = "Denis"
ocupatie = "programis"
locatie = "Bucuresti"

s9 = f"Ma numesc {nume}, am {virsta}, sunt {ocupatie}, din {locatie}"

var = 0.1234567890
# print("Variabila:" , f"{var: .3f}")

titlu = "Amintiri din copilarie"
autor = "Ion Creanga"

# print("Cartea  %s scrisa de %s nu mai este in stoc" % (titlu, autor))
# numar1 = 20
# print("Avem %d carti" % (numar1))


# print('1,2', end='')
# print(' ',1, "cuvint", sep='-')
# print("1,2,3")

x1 = 2.45
x2 = 3.08
suma = x1 + x2
suma_ca_intreg = int(suma)
# print(suma_ca_intreg)

prudus = x1 * x2

d1 = Decimal('1.15')
d2 = Decimal('2.15')

produs2 = d1 * d2
print(produs2)

print(prudus)
