# region 1. DP comportamentale - Iterator - concept

'''
ITERATOR
- folosit pt a crea structuri iterabile, parcurse element cu element
- structura iterabila = structura care poate fi parcursa cu un FOR
- pt implementare, trebuie sa suprascriem:
1. __iter__ -> returneaza intreaga structura care poate fi parcursa
2. __next__ -> returneaza urmatorul element din secventa iterabila
- oprim parcurgerea secventei prin declansarea exceptiei StopIteration
- acest DP este implementat by default in liste, tupluri si stringuri
'''


# endregion

# region 2. Exemplu Iterator1: Parcurgerea unei liste in ordinea adaugarii elementelor sau ordine inversa adaugarii

class TraverseIterator:
    position = None  # stocheaza pozitia curenta din parcurgere
    reverse = False  # controleaza ordinea in care parcurgem lista - False = ordinea adaugarii elementelor;

    # True = ordine inversa

    def __init__(self, collection, reverse):
        self.collection = collection  # lista pe care o vom parcurge
        self.reverse = reverse
        self.position = -1 if reverse == True else 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            # la fiecare iteratie, se efectueaza:
            value = self.collection[self.position]  # extragem valoarea din pozitia curenta
            self.position += -1 if self.reverse == True else 1  # actualizam pozitia
            # daca suntem in reverse, mergem inapoi in cadrul listei (scadem 1)
            # daca suntem in parcurgere normala, inaintam in lista (adaugam 1)
        except IndexError:  # odata ce parcurgem toata lista, pozitia va ajunge sa reprezinte un index prea mare care nu exista
            raise StopIteration()

        return value


collection = TraverseIterator(["first", "second", "third"], True)
for item in collection:
    print(item)


# endregion

# region 3. Exemplu Iterator2: Sirul lui Fibonacci

# Primele n nr din sirul lui fibonacci - fiecare nr este suma
# celor 2 nr anteriore - ex: 0,1,1,2,3,5,8,13 etc

class FibonacciIterator:

    def __init__(self, n):
        self.counter = n  # cate nr generam
        self.current_number = 0  # numarul fibonacci pt iteratia curenta
        self.next_number = 1  # numarul fibonacci care urmeaza

    def __iter__(self):
        return self  # self reprezinta acea structura care poate fi iterata

    # (cartea in sine, ale carei pagini le parcurgem cu __next__ )

    def __next__(self):
        if self.counter == 0:
            raise StopIteration  # am generat deja nr cerut de nr fibonacci

        self.counter -= 1
        new_fibonacci_number = self.current_number + self.next_number
        self.current_number = self.next_number
        self.next_number = new_fibonacci_number
        '''
        0,1,1,2,3
        self.current_number = 1
        self.next_number = 2
  
        new_fibonacci_number = 1+2 = 3
        self.current_number = 2
        self.next_number = 3
        '''

        return self.current_number


fib_100 = FibonacciIterator(100)
for fib in fib_100:
    print(fib)

# endregion