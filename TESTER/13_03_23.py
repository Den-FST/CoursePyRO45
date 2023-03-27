"""
In python toate struncturile de date sunt Obiecte!!!

Variabile:
- O variabila este un simbol(nume) care reprezinta un set de valori sau o valoare dintr-un program
- variabilele nu poate fi declarata incepand cu un numar sau un simbol
variabila1 = "data"
- putem face operatii cu ajutorul lor

variabila1 = "data"

alta_variabila = 2

x = 6
y = 7

"""

"""
Tipuri de date:
1. stringuri (str) - siruri de caractere.
 - stringurile sunt definite cu ghilimele simple sau ghilimele duble

Operatii de baza asupra stringurilor:
- Cum aflam prima litara dintr-un string?
Cu ajutorul operatorului de indexare: []
var1 = 'Aceasta este o variabila'
Prima litera poate fi obtinuta pentru var1 cu accesarea indexului 0: var1[0]

- Cum aflam prima si cea cea dea 6 litera, incluzand pe cele dintre ele?
Pentru a afla prima litera si urmatoarele 6 se poate accesa folosind  operatorul slicing:
var1[0:7]

- Cum aflam daca un substring este in interiorul unui alt substring ?
string1 = 'un string intr-un alt string "Salut" '
substring1 = ' alt  '

print(substring1 in string1)

- Cum capitalizam un string ?
elvis = 'elvis'
elvis.capitalize()

- Cum transformam un string intr-un sir de caractere cu litere mici?
website = 'GooGle.cOm
website.lower()

- Cum transformam un string intr-un sir de caractere cu litere mari?
website = 'GooGle.cOm
website.upper()
 
- Cum putem obtine lungimea unui string ?
website = 'GooGle.cOm
len(website)

- Cum putem inlocui intr-un string cu un substring?
propozitie = "Ana are mere si portocale."
propozitie.replace("portocale", "pere")

- Cum putem afla lista de cuvinte dintr-un string ?
propozitie = "Ana are mere si portocale"
propozitie.split()

- cum putem intoare de la ultimul element la primul?
website = 'GooGle.cOm
website[::-1]

!!!Va rog sa invatati despre slicing
class slice(start, stop, step=1)
Return a slice object representing the set of indices specified by range(start, stop, step). 
The start and step arguments default to None. Slice objects have read-only data attributes start, stop, 
and step which merely return the argument values (or their default). They have no other explicit functionality;
however, they are used by NumPy and other third-party packages. Slice objects are also generated when extended
indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate
version that returns an iterator.

Returnează un obiect slice (fâșie) care reprezintă setul de indici specificat prin intervalul (range) (start, stop, step).
Argumentele start și step au implicit valoarea None. Obiectele slice au atribute de date read-only start, stop și step
care pur și simplu returnează valorile argumentelor (sau valorile lor implicite). Aceste obiecte nu au alte 
funcționalități explicite; cu toate acestea, ele sunt utilizate de NumPy și alte pachete terțe. Obiectele slice sunt,
de asemenea, generate atunci când este utilizată sintaxa de indexare extinsă. De exemplu: a[start:stop:step] 
sau a[start:stop, i]. Consultați itertools.islice () pentru o versiune alternativă care returnează un iterator.


Exemple: 
'Elvis'
'Alin'
'Alex'
'Dragos'
"Andreea"
"Alina"
"Alexandra"

"Saru'mana"

'un string intr-un alt string "Salut" '

nume = "Jari"
prenume = "Florin"

nume_plus_prenume = nume+prenume

print(nume_plus_prenume)
print(len(nume_plus_prenume))

2.Bool(boolean)
- Ce este un bool?
 Este un tip de date ce poate lua 2 valori posibile:
  - True(1)
  - False(0)

- cea mai mare utilizare este cea de comparatie: ==


3. Integer(int) numerele intregi
- reprezinta numerele intregi fara vircuga.
- include toate numere intregi, limitat atat pozitive cat si negative

Exemplu:
x = 5
y = -10

Ce oeratii pot fi facute cu int?

Adunare: a + b
Scădere: a - b
Înmulțire: a * b
Împărțire întreagă: a // b
Împărțire cu rezultat real: a / b
Restul împărțirii: a % b
Putere: a ** b
Operații logice: <, >, <=, >=, ==, !=


4. Float(numerele cu zecimale, fractii)
- sunt reprezentate de numerele cu virgula mobila
x = 5.5
y = 5.232323232323

Pot fi reprezentate pana la 15 cifre semnificative dupa virgula.
In python este definita de punct(.)


5. Liste(o structura de date ce stocheaza o colectie ordonata de elemente)

Cum definim o lista ?
- cu paranteze patrate
list1 = []
list2 = [1, 2, 3, 4,]

Cum accesam primul element din lista?
cu ajutorul indexului
l = [1, 2, 3, 4,]
primul element:
l[0]
Primul element din index este intotdeana 0, daca nu il schimbam noi.

Operattii si functii utile:
Adaugarea unui element la sfarsitul unei liste:
l = [1, 2, 3, 4,]
l.append(5)

Cum stergem un element dintr-o lista?
- remove nu intoare elementul sters, ia valoarea respectiva ca parametru
l = [1, 2, 3, 4,]
l.remove(1) - sterge valoarea 1 din lista
- pop intoarce elementul sters, pop foloseste indexul elementului nu voaloarea
l.pop(0) - sterge primul element din lista

Cum sortam o lista?
l = [3,7,5,4,2,9]
lr = sorted(l, reverse=True)
print(lr)
- Sorted nu sorteaza lista si o asigneaza catre aceasta

l.sort()
- sorteaza lista si o salveaza sortata

- cu ajutorul parametrului reverse=True putem sorta descendent
l.sort(reverse=True)
sorted(l, reverse=True)


6. Tupla(tuple)
Tupla este o structura de date asemanatoare cu lista. Diferenta majora este ca tupla nu poate fi modificata odata ce este
definita.

my_tuple = (1,2,3,4)
mytuple[0]

Nu se poate adauga sau nu se poate sterge un element dintr-o tupla.

Pentru ca este un tip de date sigur si imutabil.

elvis_t = ('Elvis', 'Munteanu', '12313123123')

7. Set(set)
O structura de date neordonata stocheaza elemente unice.

Definim setul cu acolade {}
set1 = {}
set1 = {2,3,4,5}
set1 = {2,3,4,5,2,3,4,5,2,3,4,5,} # adauga doar {2, 3, 4, 5}

Cum adaugam intr-un set:
set1.add(6)
set1.remove(2) # sterge elementul cu valoarea 2


set1 = {1,2,3,4,5}
set2 = {0,2,4,5,6,7}

print(set1 | set2)  # uniunea
print(set1 & set2)  # intersectia
print(set1 - set2)  # diferenta
print(set2 - set1)  # diferenta

Putem verifica daca un element este in set


el = 3

el in set1


8. Dictionar(dict)
Ce este un dictionar ?
Este o structura de date care stocheaza perechi cheie valoare!
Cheile trebui sa fie unice si imutabile: (str, int, float, tuple)

Cum sunt definite dictionarele?

dict1 = {}
dict1 = dict()
persoana = {'nume': 'Marian', 'prenume': 'Georgescu', 'varsta': 25, 'oras': 'Iasi'}

putem afla cheile unui dictionar?
persoana.keys()

cum aflam valorile unui dictionar?
persoana.values()

cum aflam elementele key-value din dictionar?
persoana.items()

cum aflam valoarea unui element?
persoana.get('nume') -> primim valoarea
persoana['nume']

Putem verifica daca o cheie sau o valaore exista in dictionar:
if 'nume' in persoana.keys():
    print(persoana['nume'])

if 'Marian' in persoana.values():
    persoana['nume'] = 'Cezar'
    print(persoana['nume'])
    
Cum adaugam sau unim 2 dictionare?
persoana.update(persoana_detalii)

Putem sterge un dictionar:
persoana.clear()


9. Functia (o sectiune de cod care paote fi apelata din alte sectiuni ale programului)
Functia grupeaza o logica si o anumita sarcina pentru a face codul usor de gestionat si de utilizat

Functia este definita cu ajutorul cuvantului 'def'
Functia are un nume 
Functia are un set de parametri, care pot fi optionali
Functia returneaza intotdeauna un rezultat cu ajutorul cuvantului 'return'
Chiar daca nu ii definim un return, aceasta returneaza None

'None' - reprezentarea lipsei unei valori sau a unei referinte.
- Numele unei functii in python trebuie sa inceapa cu litere si sa nu includa caractere speciale.

# definirea unei functii
def afiseaza_mesaj():
    return 'Acesta este un print'


def afiseaza_mesaj_print():
    x = 'Acesta este un print'
    return x

# rezultat1 = afiseaza_mesaj()
rezultat2 = afiseaza_mesaj_print()
#
# print(rezultat1)
print(rezultat2)


def adunare_cu_2(a=3):
    return a + 2

print(adunare_cu_2(5))
"""