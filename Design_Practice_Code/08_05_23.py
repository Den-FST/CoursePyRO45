# region 0. Rezolvare tema docstring

# Tema: Scrieti un docstring pt urmatoarea functie
import datetime
import time
from abc import abstractmethod, ABC


def validate_name(n):
    '''
    Valideaza numele ca format si lungime

    Descrierea parametrilio
    n (str): reprezinta numele pe care il vom valida

    Descrierea outputului
    afisaza lista de cuvinte extrase din input
    return (boolean) - True daca primul cuvant este Title case si lungime intregului nume are minim 3 caractere altfel False

    Exemple
    validate_name("Ana Maria") return True
    validate_name("A na Maria") return True
    validate_name("ana") return False
    validate_name("An") return False
    '''
    substrings = n.split()
    print(substrings)
    for substring in substrings:
        if substring.istitle() and len(n) >= 3:
            return True
        else:
            return False


# endregion

# region 1. AUTO-FORMATTERS

# se ocupa de asezarea in pagina (code layout, spatii goale, linii goale etc)

# pip install black

# endregion

# region 2. Acronime clean code

'''
SOLID

S = Single responsability principle
= fiecare functie trebuie sa faca un singur lucru = sa aiba o singura responsabilitate
- daca ajungem la o functie care face 5 lucruri, o spargem in 5 functii mai mici

O = Open-closed principle
= open to inheritance, closed to modification
- preferam sa mostenim o clasa si sa adaugam un atribut/o metoda pe parcurs in clasa copil, decat sa modificam
clasa initiala

L = Liskov substitution principle
= obiectele clasei parinte trebuie sa poata fi inlocuite mereu cu obiecte din clasa copil, fara a produce erori
in aplicatie

I = Interface segregation principle
= segregarea functionalitatii pana la cel mai specific nivel
- vrem functii cu cate un singur rol, cat mai specific

D = Dependency Inversion principle
= high-level modules nu trebuie sa depinda de low-level modules, ambele trebuie sa depinda de abstractizari
- high-level module se foloseste de low-level module
'''


# Exemplu Dependency Inversion

# versiune NOT clean code

class Bread:  # clasa care este low-level module - este considerata low-level pt ca este folosita in alta parte

    def bake(self):
        print("Smells like bread")


def cook():  # functia cook() este un high-level module
    bread = Bread()
    bread.bake()


cook()

# versiune clean code - introducerea unui layer de abstractizare

'''
Pt a fi abstracta, o clasa trebuie sa:
1. mosteneasca ABC
2. aiba o metoda astracta (marcata cu @abstractmethod)
'''


class Bakeable(ABC):  # abstractizarea

    @abstractmethod
    def bake(self):
        pass


class Bread(Bakeable):  # low-level module

    def bake(self):
        print("Smells like bread")


class Cookies(Bakeable):  # low-level module

    def bake(self):
        print("Smells like cookies")


def cook(bakable):  # high-level module
    bakable.bake()


cookies = Cookies()
bread = Bread()
cook(cookies)
cook(bread)

'''
Alte acronime
KISS = Keep It Simple and Stupid
DRY = Don't Repeat Yourself
YAGNI = You Ain't Gonna Need It
'''

# endregion

# region 3. Design Patterns - generalitati

'''
DP = solutie universala pt o problema recurenta in procesul de dezvoltare al unei aplicatii
DP au fost instaurate de GoF (Gang of Four) in cartea "Design Patterns"
Categorii:
1. Creational DP = creationale = cum creem obiectele unei clase
2. Structural DP = structurale = cum organizam clasele care au legatura una cu alta
3. Behavioral DP = comportamentale = cum gestionam responsabilitatea instantelor de clasa

Tutoriale cu toate DP
https://python-patterns.guide/
https://www.geeksforgeeks.org/python-design-patterns/
https://refactoring.guru/design-patterns/catalog

1. CREATIONAL DP
Singleton
Builder
Factory
Factory Method
Abstract Factory
Prototype

2. STRUCTURAL DP
Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

3. BEHAVIORAL DP
Chain of Responsability
Command
Interpreter
Iterator
Mediator
Memento
Observer
State
Strategy
Template
Visitor
'''

# endregion

# region 4. Creational DP - Singleton

'''
Singleton - DP folosit cand avem ca si conditie sa creem maxim un singur obiect dintr-o clasa
- scenariu: orice situatie de monopol (ex: metroul din Romania)
- highlights implementare:
1. suprascrierea metodei magice __new__
2. nested class (clasa interna)
'''


class MetrouRomania:
    # nested class
    class Singleton:

        def __init__(self, nume_metrou):
            self.nume_metrou = nume_metrou

    instance = None  # aceasta va fi unica instanta a clasei

    # suprascriem __new__
    def __new__(cls, nume_metrou):
        if not MetrouRomania.instance:  # exista deja o instanta de MetrouRomania?
            MetrouRomania.instance = MetrouRomania.Singleton(nume_metrou)  # daca nu exista, atunci creem instanta

        # daca exista deja instanta, atunci o returnam
        print(MetrouRomania.instance)
        return MetrouRomania.instance


metrorex = MetrouRomania("Metrorex")
metrouSDA = MetrouRomania("SDA")
print(metrorex.nume_metrou, metrouSDA.nume_metrou)

# endregion

# region 5. Exercitiu Singleton

'''
Ex: Scriem o clasa Logger care implementeaza Singleton
- in clasa interna Singleton vom avea __init__ care primeste ca parametru numele fisierului
in care vom scrie logg-uri
- pe langa __init__ vom avea si metoda log_time - care scrie data si ora curenta
'''


class Logger:
    # nested class
    class Singleton:

        def __init__(self, nume_file):
            self.nume_file = nume_file

        def log_time(self):
            with open(self.nume_file, "a") as file:
                file.write(str(datetime.datetime.now()))
                file.write("\n")

    instance = None  # aceasta va fi unica instanta a clasei

    # sucrascriem __new__
    def __new__(cls, nume_file):
        if not Logger.instance:  # exista deja o instanta de MetrouRomania?
            Logger.instance = Logger.Singleton(nume_file)  # daca nu exista, atunci creem instanta

        # daca exista deja instanta, atunci returnam.
        print(Logger.instance)
        return Logger.instance


logger1 = Logger("log.txt")
logger1.log_time()
time.sleep(5)
logger2 = Logger("log2.txt")
logger2.log_time()

# endregion

# region 6. Builder

'''
- separa partea de constructie a obiectului de partea de reprezentare
- folosit cand vrem sa reprezentam acelasi obiect in mai multe feluri
'''


# Ex: 3 reprezentari pt un string: UPPERCASE, lowercase, hexa

class Builder:  # clasa parinte pe care o va mosteni fiecare clasa care va reprezenta o reprezentare

    def build(self, element):  # construieste reprezentarea caracter cu caracter (element = caracter din string)
        pass

    def get_result(self):
        pass


# scriem clasele copil care reprezinta cate o reprezentare

class UpperBuilder(Builder):

    def __init__(self):
        self.result_upper = ''  # pornim de la empty string

    def build(self, element):  # construieste reprezentarea caracter cu caracter (element = caracter din string)
        self.result_upper += element.upper()

    def get_result(self):
        return self.result_upper


class LowerBuilder(Builder):

    def __init__(self):
        self.result_lower = ''  # pornim de la empty string

    def build(self, element):  # construieste reprezentarea caracter cu caracter (element = caracter din string)
        self.result_lower += element.lower()

    def get_result(self):
        return self.result_lower


class HexaBuilder(Builder):

    def __init__(self):
        self.result_hexa = ''  # pornim de la empty string

    def build(self, element):  # construieste reprezentarea caracter cu caracter (element = caracter din string)
        self.result_hexa += f"0x{ord(element):02x}"

    def get_result(self):
        return self.result_hexa


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_builder(self, builder):  # pt a face switch intre reprezentari
        self.builder = builder

    def construct(self):  # construim stringul conform reprezentarii alese
        string_to_print = f"{self.name} is {self.age} years old"

        for char in string_to_print:
            self.builder.build(char)  # construiesc efectiv reprezentarea

    def get_result(self):
        return self.builder.get_result()


p = Person("Denis", 35)

upper = UpperBuilder()
lower = LowerBuilder()
hexa = HexaBuilder()

for builder in [upper, lower, hexa]:
    p.set_builder(builder)
    p.construct()
    print(p.get_result())

# endregion