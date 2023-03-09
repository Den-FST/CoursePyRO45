"""
De preferat pentru acest exercitiu este sa folosit TDD(TestDrivenDevelopment)
Asta inseamna sa scrieti testul pentru pasul initial si apoi scrierea codului pentru trecerea testului respectiv.

Clasa Bucatarie trebuie sa incluna un nume si un dictionar numit Inventar care sa contina numele si cantitatea ingredientelor disponibile.
Sa se poata adauga cantitati de ingrediente in inventar.
Sa se poata scadea cantitati de ingrediente din inventar.
In clasa Bucatarie sa se poata defini o reteta sub forma unui dictionar cu un nume si o lista de ingrediente necesare pentru a o realiza, impreuna cu cantitatile aferente.
Sa se poata crea un obiect de tip ProdusFinal care are un nume si contine un numar de ingrediente din reteta (cu cantitatile aferente) necesare pentru a fi consumate.
Produsul finit trebuie sa fie adaugat intr-o lista a produselor finite deja create.


Pasi pentru crearea acestui exercitiu:
 + Definirea clasei Bucatarie si atributele sale (nume si dictionarul inventar).
 + Adaugarea metodei de adaugare a ingredientelor in inventar.
 + Adaugarea metodei de scazut cantitatile de ingrediente din inventar.
 + Definirea clasei Reteta, care va contine numele si o lista de ingrediente necesare (nume si cantitatile aferente).
 + Definirea metodei in clasa Bucatarie care poate crea o reteta si o adauga in lista retetelor disponibile.
 + Definirea clasei ProdusFinal care va contine numele si ingredientele folosite din reteta (Poate mosteni Reteta).
 + Definirea metodei care va crea un obiect de tip ProdusFinal pe baza unei retete si va scadea cantitatile necesare din inventar.
 + Adaugarea produsului finit creat intr-o lista a produselor finite deja realizate.
 + Scrierea testelor pentru a verifica functionalitatile implementate in script.


Extra:
Creati un fisier, sau fisiere multiple in care sa salvati retelete, inventarul si produsele finite deja create.
"""



class Bucatarie:
    def __init__(self, nume):
        self.nume = nume
        self.ingrediente = {}

    def adauga_ingredient(self, ingredient, cantitate):
        if ingredient in self.ingrediente:
            self.ingrediente[ingredient] += cantitate
        else:
            self.ingrediente[ingredient] = cantitate

    def fa_reteta(self, reteta):
        for ingredient, cantitate in reteta.items():
            if ingredient not in self.ingrediente or self.ingrediente[ingredient] < cantitate:
                print(f"Lipsesc ingredientele pentru a face reteta '{reteta}'.")
                return False
        for ingredient, cantitate in reteta.items():
            self.ingrediente[ingredient] -= cantitate
        print(f"Reteta '{reteta}' a fost realizata cu succes!")
        return True


# Crearea unei instanțe de bucătărie
bucatarie = Bucatarie('Bucatarie lui Ion')

# Adăugarea de ingrediente
bucatarie.adauga_ingredient('faina', 500)
bucatarie.adauga_ingredient('oua', 6)
bucatarie.adauga_ingredient('zahar', 200)
bucatarie.adauga_ingredient('unt', 250)

# Facerea unei rețete
reteta1 = {'faina': 200, 'oua': 2, 'zahar': 100, 'unt': 100}
bucatarie.fa_reteta(reteta1)  # Va afișa "Reteta '{'faina': 200, 'oua': 2, 'zahar': 100, 'unt': 100}' a fost realizata cu succes!"
print(reteta1)
# Verificarea cantității de ingrediente rămase


# Am verificat daca folosesc cantitatea mai mare decit existanta ce mesaj da:
# print(bucatarie.ingrediente)  # Va afișa "{'f
# reteta2 = {'faina': 200, 'oua': 8, 'zahar': 100, 'unt': 100}
# bucatarie.fa_reteta(reteta2)  # Va afișa "Reteta '{'faina': 200, 'oua': 2, 'zahar': 100, 'unt': 100}' a fost realizata cu succes!"