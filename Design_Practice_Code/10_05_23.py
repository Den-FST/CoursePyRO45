# region 1. DP comportamentale - conceptual

'''
MEDIATOR
- se ocupa cu simplificarea comunicarii dintre obiecte
- reduce nr de dependinte dintre obiecte
- obiectele sunt independete unele de altele, insa comunica in continuare
- problema care poate aparea: Mediatorul poate deveni GOD OBJECT (un obiect cu prea multe responsabilitati) - antipattern
'''
import pickle
from abc import ABC, abstractmethod

'''
OBSERVER (spionul)
- observerul reactioneaza la un state change al observabilului
- comparatie: paianjenul (observer) si panza lui (observabilul)
'''

'''
STATE
- un obiect reactioneaza cand propria stare se schimba
- exemplu: bubble gum machine - la introducerea monedei, bubble gum machine returneaza o guma
'''

'''
STRATEGY
- https://auth0.com/blog/strategy-design-pattern-in-python/
- folosit in luarea deciziilor in timpul executiei aplicatiei
- noi definim un set de strategii, insa strategia finala va fi aleasa la runtime (nu putem intui exact rezultatul
inainte de a da RUN)
'''

'''
TEMPLATE
- https://refactoring.guru/design-patterns/template-method/python/example
- ne ofera scheletul unei operatiuni
- dpdv implementare, vom avea o clasa abstracta cu metode abstracte si metode normale; clasele copil vor mosteni
aceasta clasa abstracta si vor suprascrie obligatoriu metodele abstracte, iar optional pot suprascrie si metodele normale
din clasa parinte
'''

'''
VISITOR
- 2 entitati principale:
1. Clasa abstracta cu implementari concrete - fiecare clasa concreta contine o resursa de care vizitatorul are nevoie +
o metoda de acceptare a vizitatorului
2. Vizitatorul - are nevoie de resursa de la clasele concrete, insa o poate accesa doar daca indeplineste conditia din
metoda accept()
'''

# endregion

# region 2. DP comportamentale - Command - implementare

'''
COMMAND
- exista un intermediar intre cel care face o cerere (client) si cel care satisface aceasta cerinta (executantul)
- exemplu: telecomanda ca intermediar intre cel care vrea schimbarea programului si televizor
'''


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# clasa abstracta Command poate fi concretizata in oricate clase copil - noi vom crea SimpleCommand si ComplexCommand

class SimpleCommand(Command):
    '''
    Executarea unei comenzi simple: printarea unui string
    '''

    def __init__(self, str_to_print):
        self.str_to_print = str_to_print

    def execute(self):
        print(f"Simple command: printing {self.str_to_print}")


class Receiver:
    '''
    Clasa utilitara care va fi folosita de ComplexCommand
    '''

    def do_something(self, task1):
        print(f"Receiver works on {task1}")

    def do_something_else(self, task2):
        print(f"Receiver works on {task2}")


class ComplexCommand(Command):
    '''
    Executarea unei comenzi complexe prin intermediul unui receiver, in 2 pasi
    '''

    def __init__(self, receiver, step1, step2):
        self.receiver = receiver
        self.step1 = step1
        self.step2 = step2

    def execute(self):
        print("Complex command is executed by receiver object")
        self.receiver.do_something(self.step1)
        self.receiver.do_something_else(self.step2)


class Invoker:
    '''
    Intermediarul dintre client (noi, care cerem o comanda simpla sau complexa) si executantul (metoda execute,
    suprascrisa in cele 2 clase concrete)
    '''

    def __init__(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


simple_command = SimpleCommand("Modul Design Patterns & Best Practices")
invoker = Invoker(simple_command)
invoker.invoke()

complex_command = ComplexCommand(Receiver(), step1="du-te pana jos", step2="adu mingea")
invoker2 = Invoker(complex_command)
invoker2.invoke()

# endregion

# region 3. DP comportamentale - Memento - implementare

'''
MEMENTO
- gestioneaza snapshots (memento objects) ale unui obiect
- prin acest DP, putem sa ne intoarcem la o stare din trecut a unui obiect
- dpdv tehnic, folosim serializarea pt implementarea acest DP

Serializare = transformarea unui obiect python (instanta din clasa creata de mine / lista / dictionar etc) in secventa
de bytes (stream)
Deserializare = citirea unei secvente de bytes (stream) si re-crearea obiectului python
'''


class Person:

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def create_snapshot(self):
        '''
        pickle este pachetul care se ocupa de serializare in python
        .dumps() este functia care serializeaza
        self.__dict__ este o dunder variable (dunder = double underscore; variabile magice, cu semnificatii mai
        speciale) reprezentand un dictionar care contine toate atributele specifice instantei respective
        '''

        return pickle.dumps(self.__dict__)

    def restore_to_snapshot(self, snapshot):
        self.__dict__.update(pickle.loads(snapshot))  # .loads() deserializeaza


p = Person()
print(p.age)

snapshot1 = p.create_snapshot()
p.age = 25
print(p.age)

p.restore_to_snapshot(snapshot1)
print(p.age)


# Varianta optimizata a DP Memento cu scriere in fisier cu extensia pickle
class Person:
    def __init__(self, name="", age=0) -> None:
        self.name = name
        self.age = age

    def create_snapshot(self, file_name):
        with open(file_name, "wb") as file:
            # folosim functia dump() ptr serializare cu scriere in fisier
            pickle.dump(self.__dict__, file)

    def restore_to_snapshot(self, file_name):
        with open(file_name, "rb") as file:
            snapshot = pickle.load(file)
            self.__dict__.update(snapshot)


print("")
p = Person()
print(p.age)
snapshot1 = p.create_snapshot("fisier.pickle")
p.age = 25
print(p.age)
p.restore_to_snapshot("fisier.pickle")
print(p.age)

# endregion