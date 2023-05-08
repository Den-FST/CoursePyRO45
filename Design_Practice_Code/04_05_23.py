'''
DESIGN PATTERNS AND GOOD (BEST) PRACTICES - 14h
'''

# region 1. Best Practices

'''
= Recomandari py a scrie un cod ca un profisionist

In Python, best practices sunt adunate in documente numipte PEP - Python Enhancement Proposal

PEP 20 - Zen of Python


'''

# import this

# region 2

'''
PEP 8

= recomandari pt a scrie clean code


Naming conventions
1. functii - snake_case = litere mici + underscore pt despartirea cuvintelor
2. variabile - snake_case
3. clase - CamelCase/PascalCase = majuscula la inceputul cuivintului + fara despartirea cuvintelor 
'''


# region 3. Comments


class Person:

    '''
    Clasa Persoana are atributele name, cpn si age
    Cu metode getter, setter si o metoda statica (docstring)
    '''

    def __init__(self, name, cnp, age):
        self.name = name
        self.__cnp = cnp
        self.age = age

    '''
    Acesta este un comentariu
    multiline
    '''

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, cnp_nou):
        if len(cnp_nou) == 13:
            self.__cnp = cnp_nou
        else:
            print('CNP nevalid')  # afiseaza mesaj pentru valoare nepotrivita

    @cnp.deleter
    def cnp(self):
        del self.__cnp

    # O metoda statica pentru validarea numelui
    @staticmethod
    def validate_name(n):
        if n[0].isupper() and len(n) >= 3:
            return True
        else:
            return False

# print(Person.__doc__)

# region 4. PEP 257

'''
reguli de scriere a docstringurilor (documentatie de cod)

'''

def my_function(param):
    '''
    Scopul funciei

    Descrierea parametrilor
    :param type + alte detalii daca exista

    :return:

    (Optional) Side effects - daca aceasta functie afecteaza orice alta parte a codului

    Usage Example + expected output
    '''


# region 5. Tips & Tricks

# slicing
my_str = "abc"
if my_str[0] == "a":
    print("My str starts with A")
else:
    print("My str start with some else")

# metoda specifica (clean code)
if my_str.startswith("a"):
    print('Starts with a')
else:
    print('Starts with something else')

# 2. Folosirea unui logical context
#Exemple de logical context:
# "" (empty string) este echivalent cu False
# 0 este echivalent cu False; 1 este echivalent cu True
# [] (empty list) este echivalent cu False

if "":
    print("non-empty string")
else:
    print("empty string")

if 0:
    print("non-zero")
else:
    print("zero")

# 3. Folosim "if x is not None" in loc de "if x"

x = None
if x is not None:
    print("not none")
else:
    print('None')

# region 6. Linters


'''
DESIGN PATTERNS AND GOOD (BEST) PRACTICES - 14H
'''

# region 1. Best Practices + PEP 20

'''
= recomandari pt a scrie un cod ca un profesionist

In Python, best practices sunt adunate in documente numite PEP - Python Enhancement Proposal

PEP 20  - Zen of Python
https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/
'''

import this  # obtinem cele 19 principii care stau la baza programarii python

# endregion

# region 2. PEP 8

'''
https://peps.python.org/pep-0008/
= recomandari pt a scrie clean code
'''

'''
Naming conventions
1. functii - snake_case = litere mici + underscore pt despartirea cuvintelor (ex: read_file)
2. variabile - snake_case (ex: current_user)
3. clase - CamelCase/PascalCase = majuscula la inceputul cuvantului + fara despartirea cuvintelor (ex: EmployedPerson)
4. metode - snake_case (ex: plateste_rata)
5. constante - uppercase + underscore pt despartirea cuvintelor (ex: MAX_VALUE)
6. scripturi - snake_case (ex: my_script.py)
7. pachete - lowercase fara despartirea cuvintelor (ex: mypackage)
'''

'''
Code Layout
- lasam 2 linii goale inainte de definirea unei noi functii/clase
- lasam o singura linie intre pasii aceleiasi functii/metodele aceleiasi clase
- 79 de caractere per linie de cod - o linie mai lunga o spargem cu \
- CTRL Alt L - formateaza codul dpdv spatii
- inconjuram cu space operatiile: =, +=, -=, ==, <, >, is, and etc.
'''

# endregion

# region 3. Comments

'''
1. comentariu inline - pe aceeasi linie cu codul, f succinte
2. block comments - pe o linie separata deasupra codului - explica urmatoarea linie/urmatoarele linii de cod
3. multiline comment - se marcheaza prin 3 perechi de ' sau "
* daca un multiline comment apare imediat dupa "def functie/clasa:", atunci vorbim despre un docstring, nu despre comentariu
'''


class Person:
    def __init__(self, name, cnp, age):
        self.name = name
        self.__cnp = cnp
        self.age = age

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, cnp_nou):
        if len(cnp_nou) == 13:
            self.__cnp = cnp_nou
        else:
            print('CNP nevalid')

    @cnp.deleter
    def cnp(self):
        del self.__cnp

    @staticmethod
    def validate_name(n):
        if n[0].isupper() and len(n) >= 3:
            return True
        else:
            return False


# Exercitiu: Scrieti un comentariu inline, un comentariu block si un multiline comment pe clasa de mai sus
# Rezolvare

class Person:
    '''
    Clasa Persoana are atributele name, cpn si age
    Cu metode getter, setter si o metoda statica (docstring)
    '''

    def __init__(self, name, cnp, age):
        self.name = name
        self.__cnp = cnp
        self.age = age

    '''
    Acesta este un comentariu
    multiline
    '''

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, cnp_nou):
        if len(cnp_nou) == 13:
            self.__cnp = cnp_nou
        else:
            print('CNP nevalid')  # afiseaza mesaj pentru valoare nepotrivita

    @cnp.deleter
    def cnp(self):
        del self.__cnp

    # O metoda statica pentru validarea numelui
    @staticmethod
    def validate_name(n):
        if n[0].isupper() and len(n) >= 3:
            return True
        else:
            return False


print(Person.__doc__)

# endregion

# region 4. PEP 257

'''
= reguli de scriere a docstringurilor (documentatie de cod)

Docstringul:
- il scriem cu 3 seturi de " sau '
- trebuie sa fie primul statement din functie/clasa/metoda - daca il scriem oriunde altundeva pe parcursul
functiei/clasei/metodei, atunci devine multiline comment
- il accesam prin __doc__
'''


# Template docstring pt functie

def my_function(param):
    '''
    Scopul functiei

    Descrierea parametrilor
    :param type + alte detalii daca exista

    Descrierea outputului
    :return

    (Optional) Side effects - daca aceasta functie afecteaza orice alta parte a codului (ex: daca este folosita
    in cadrul altei functii)

    Usage Example + expected output
    '''


# Tema: Scrieti un docstring pt urmatoarea functie
def validate_name(n):
    substrings = n.split()
    print(substrings)
    for substring in substrings:
        if substring.istitle() and len(n) >= 3:
            return True
        else:
            return False


# endregion

# region 5. Tips & Tricks

# 1. inlocuim slicingul cu metode specifice

# slicing
my_str = "abc"
if my_str[0] == "a":
    print("My str starts with A")
else:
    print("My str starts with something else")

# metoda specifica (clean code)
if my_str.startswith("a"):
    print("My str starts with A")
else:
    print("My str starts with something else")

# 2. Folosirea unui logical context
# Exemple de logical context:
# "" (empty string) este echivalent cu False
# 0 este echivalent cu False; 1 este echivalent cu True
# [] (empty list) este echivalent cu False

if "":
    print("non-empty string")
else:
    print("empty string")

if 0:
    print("non-zero")
else:
    print("zero")

if []:
    print("non-empty list")
else:
    print("empty list")

# 3. Folosim "if x is not None" in loc de "if x"
x = None
if x is not None:
    print("not none")
else:
    print("none")

# endregion

# region 6. Linters

# = program care analizeaza codul si identifica erori/probleme legate de clean code (PEP8)
# exemple: flake8, pycodestyle, pylint

# endregion