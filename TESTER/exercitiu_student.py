"""
Creati o clasa "Student" cu urmatoarele atribute: nume, prenume, varsta, medie.

Cerinte:

Creati un set de teste folosind modulul Pytest care sa acopere toate functionalitatile metodelor din clasa Student.
Creati constructorul clasei care primeste numele, prenumele, varsta si media studentului ca parametri. Setati valorile atributelor corespunzatoare.
Creati o metoda "promovat" care returneaza True daca media studentului este mai mare sau egala cu 5 si False in caz contrar.
Creati o metoda "prezentare" care afiseaza numele, prenumele, varsta si media studentului in formatul "Nume Prenume, varsta ani, media: X".
Creati o metoda "calculeaza_media" care calculeaza media studentului pe baza notelor adaugate pana in acel moment.
Creati o metoda "adauga_nota" care primeste ca parametru o nota si o adauga la media studentului.
Creati o metoda "scade_nota" care primeste ca parametru o nota si o scade din media studentului.

Succes!

"""


class Student:

    def __init__(self, nume, prenume, varsta, note):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.note = note
        self.medie = self.calculare_medie()

    def promovat(self):
        if self.medie >= 5:
            return True
        else:
            return False

    def prezentare(self):
        return f"{self.nume} {self.prenume}, {self.varsta} ani, media: {self.medie}."

    def calculare_medie(self):
        media_notelor = sum(self.note)/len(self.note)
        return media_notelor

    def adauga_nota(self, nota):
        self.note.append(nota)

    def scade_nota(self, nota):
        if nota in self.note:
            self.note.remove(nota)

