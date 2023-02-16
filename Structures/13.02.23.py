# import os


"""
1) Date
- culoare
- an de fabricatie

2)
- C;asa: Masina

3)
- actiuni ale obiectului
- tureze
- activa luminile de avarii
- frana
"""


"""
- Clasa speciala
- om este obiect
"""

"""
- Clasa este om
- elev muncitor student subclase
- Ion obiect
- Irina obiect
"""

"""
Clasa legume
- ardei 
- ceapa
- vinete
"""

"""
Clasa mobilier
- dulap
- mese
- scaun
"""
#
# #definitia clasei
# class Pisica:
#
#     def __init__(self):
#         self.nume = "Miti"
#         self.varsta = 5
#
# pisica1 = Pisica()
# print(pisica1.nume)


# class human:
#     pass
#
# class programist(human):
#
#     def __init__(self, nume , varsta, limbaj, nivel):
#         self.nume = nume
#         self.varsta  = varsta
#         self.limbaj = limbaj
#         self.nivel = nivel
#
#     def imbatraneste(self):
#         return self.varsta + 1
#     def prezintate(self):
#         print('Eu sunt {} si am {} ani, scriu in limbajul: {}, si sunt la nivel "{}"'.format(self.nume, self.varsta, self.limbaj, self.nivel))
#     def __str__(self):
#         return ('Eu sunt {} si am {} ani, scriu in limbajul: {}, si sunt la nivel {}'.format(self.nume, self.imbatraneste(), self.limbaj, self.nivel))
#
# ion = programist("Ion", 30, "C++", "Junior")
# max = programist("Max", 37, "Java", "Middle")
#
# # print(ion)
# # print(ion.nume, ion.varsta, ion.limbaj, ion.nivel)
# # ion.prezintate()
#
# programisti = [ion, max]
#
# for programist in programisti:
#     programist.prezintate()

# #clasa parinte
# class Om:
#     def __init__(self, nume, inaltime, greutate):
#         self.nume = nume
#         self.inaltime = inaltime
#         self.greutate = greutate
#     def saluta(self):
#         print('Buna ziua! Sunt {}'.format(self.nume))
#
# #clasa copil
# class programator(Om):
#     def __init__(self, nume, inaltime, greutate, limbaje):
#         super().__init__(nume, inaltime, greutate)
#         self.limbaje = limbaje
#     def programeaza(self):
#         print('{} programeaza cu drag si spor'.format(self.nume))
#
# om1 = Om('Gigel', '1.78', 78)
# print(om1.nume)
#
# programator1 = programator('Rares', '1.80', 80, 'Python, C++, Assembly')
# # print(programator1.nume)
#
#
# programator1.saluta() # e disponibil in amindoua clase
# programator1.programeaza() # nu e disponibil in clasa Om


#              [    a   ]    [   b   ]
# 0101010101101[10111001]0011000011101010100101
# a = 1 # pozitia in RAM 500.000
# b = a
# # b = 0
# print(a, b)

#

# class Om:
#     def __init__(self, nume):
#         self.nume = nume
#         self.__nivel_acid_gastric = 100
#     def merg(self):
#         print(self.__nivel_acid_gastric)
#         print('eu merg')
#     def vorbesc(self):
#         print('eu vorbesc')
#
# om1 = Om('Alex')
# om1.merg()
# om1.vorbesc()

# with open('data.txt', 'r') as file:
#     continut = file.read()
#     print(continut)



with open('data.txt', 'r') as file:
    numar = int(file.readline(1))
    print(numar)
    numar += 1
with open('data.txt', 'w') as file:
    file.write(str(numar))


    print(numar)

