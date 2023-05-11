# region 1. Alte DP creationale - conceptual

'''
FACTORY
- ne ofera implementari concrete ale unei abstractizari
- separa crearea obiectelor de definirea abstractizarii
'''
import string

'''
FACTORY METHOD
- creem obiecte care apartin aceleiasi familii - ex: familia de jocuri Monopoly etc.
'''

'''
ABSTRACT FACTORY
- creem grupuri in interiorul aceleiasi familii
- avem un nivel in plus de abstractizare fata de Factory Method
- factory of factories
'''

'''
PROTOTYPE
- exemplu: fabrica de papusi
- imparte crearea obiectului in 2 etape:
1. crearea obiectului de baza (prototipul) care va fi clonat pt a produce noi obiecte (toate papusile arata la fel pe
banda rulanta)
2. pt fiecare clona, modificam acel atribut prin care se distinge instanta (persoanlizarea fiecarei papusi)
- dpdv tehnic, folosim pachetul copy cu functiile copy (shallow copy - copie de referinte, obiectul nu este re-creat)
si deepcopy (deep copy - ocuparea memoriei de 2 ori, obiectul fiind re-creat)
* in Python, tipurile de date primitive nu se copiaza deep - int, float, double, strings, bool
* pt a verifica tipul de copie, ne putem folosi de functia id()
'''

x = "daiana"
print(id(x))

# endregion

# region 2. DP structurale - conceptual

'''
ADAPTER
- folosit pt a crea o legatura intre 2 entitati aparent incompatibile
- https://refactoring.guru/design-patterns/adapter/python/example
'''

'''
BRIDGE
- sparge o clasa complexa in mai multe ierarhii pe care le putem gestiona independent, asigurand totodata comunicarea
dintre ele (bridge)
- folosit la aplicatii cross-platform - cand avem un controlling entity si mai multe entitati care executa taskuri de la
acest controlling entity
'''

'''
FACADE
- ofera un API simplu pt un sistem complex
- API (Application Programming Interface) = punct de acces catre sistem + iti arata si ce optiuni are sistemul
'''

'''
PROXY
- preia cererea unui client si o directioneaza catre alt serviciu
- dpdv tehnic, creem o clasa care functioneaza ca API catre alta clasa; clasa afereta lui proxy executa o parte
"utilitara" din cererea clientului si apoi directioneaza restul catre alt serviciu
'''

# endregion

# region 3. DP structural: Flyweight - implementare

'''
- minimizeaza ocuparea memoriei in scenariul in care crearea unui obiect are legatura cu un obiect de tip diferit
- ex: mai multe obiecte de tip Masina (diferentiate prin producator - VW/BMW/Audi) vor referentia acelasi obiect de tip
Motor (combustibil = Diesel) pt a salva memoria
- acest DP este util in scenarii de testing
'''


class Masina:
    def __init__(self, producator):
        self.producator = producator
        self.motor = None

    def __str__(self):
        return f"Masina {self.producator} are motor {self.motor}"


class Motor:
    def __init__(self, combustibil):
        self.combustibil = combustibil

    def __str__(self):
        return f"Motor combustibil {self.combustibil}"


motor_diesel = Motor("Diesel")
masina_vw = Masina("VW")
masina_bmw = Masina("BMW")
masina_audi = Masina("Audi")

# principiul compozitiei presupune atribuirea valorii petru atributul motor cu un obiect de tip Motor
masina_vw.motor = motor_diesel
masina_bmw.motor = motor_diesel
masina_audi.motor = motor_diesel

for m in [masina_vw, masina_bmw, masina_audi]:
    print(m, id(m.motor))

# endregion

# region 4. DP structurale: Composite & Decorator  - implementare

'''
COMPOSITE
- compunem obiecte in structuri de tip arbore si lucram cu ele ca si cum ar fi un singur obiect
- folosit in scenarii unde vrem sa reprezentam ierarhii
'''

'''
DECORATOR
- https://realpython.com/primer-on-python-decorators/
- adauga o noua functionalitate unui obiect existent la runtime
- cel mai simplu tip de decorator: functie care ia ca parametru alta functie
'''


# Ex: Folosim composite pt a reprezenta ierarhia de departamente dintr-o firma si folosim decorator pt a scrie
# cu majuscule numele departamentelor

def capitalize(func):
    def wrapper(*args):  # scopul lui wrapper este de a mapa argumentele cu functia func
        return string.capwords(func(*args))

    return wrapper  # acest wrapper este in forma de closure (frozen state al functiei interne wrapper)


class Departament:
    '''
    Aceasta clasa va fi folosita pentru a ilustra atat departamente principale, cat si subdepartamente
    '''

    def __init__(self, nume_departament):
        self.nume_departament = nume_departament
        self.sub_departamente = []

    def adauga_subdepartament(self, subdepartament):
        self.sub_departamente.append(subdepartament)

    @capitalize
    def get_nume_departament(self):
        return self.nume_departament


departament_principal = Departament("publicitate")
subdep1 = Departament("social media")
subdep2 = Departament("tv")

departament_principal.adauga_subdepartament(subdep1)
departament_principal.adauga_subdepartament(subdep2)

print(f"Departamentul {departament_principal.get_nume_departament()} are subdepartamentele: ")
for dep in departament_principal.sub_departamente:
    # print(dep.nume_departament)
    print(dep.get_nume_departament())

# endregion

# region 5. DP comportamentale - conceptual

'''
CHAIN OF RESPONSABILITY
- creeaza un lant de potentiale raspunsuri la cererea clientului
- dpdv tehnic, se implementeaza prin lista simplu inlantuita
- cererea trece prin lista de potentiale raspunsuri pana gaseste raspunsul potrivit
'''

'''
INTERPRETER
- folosit in arhitecturi care cer recunoasterea unui limbaj de programare
- se incearca clasificare unei expresii in "Terminal" (gata de a fi procesata intr-un anumit limbaj de programare)
sau "Non-terminal" (este nevoie sa spargem expresia in parti mai mici pe care vom incerca din nou sa le clasificam)
- in final, expresia este directionata catre entitatea care stie sa proceseze limbajul detectat
'''

# endregion