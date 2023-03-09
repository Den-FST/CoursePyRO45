# class Bucatarie:
#
#     def __init__(self, nume):
#         self.nume = nume
#         self.inventar = {}
#
#     def adaugare_inventar(self, nume_ingredient:str, cantitate:int):
#         if self.inventar.get(nume_ingredient):
#             self.inventar[nume_ingredient] += cantitate
#         else:
#             self.inventar[nume_ingredient] = cantitate
#         return self.inventar
#
#     def scadere_inventar(self, nume_ingredient: str, cantitate: int):
#         if nume_ingredient not in self.inventar or self.inventar[nume_ingredient] < cantitate:
#             print(f'Nu exista cantitatea suficienta pentru a efectua operatia! ')
#             return
#         else:
#             self.inventar[nume_ingredient] -= cantitate
#     def fa_receta(self, receta):
#         for nume_ingredient, cantitate in receta.items():
#             if nume_ingredient not in self.inventar or self.inventar[nume_ingredient] < cantitate:
#                 print(f"Lipsesc ingredientele pentru a face receta '{receta}'.")
#                 return
#         for ingredient, cantitate in receta.items():
#             self.inventar[ingredient] -= cantitate
#         print(f"Reteta '{receta}' a fost realizata cu succes!")
#
# # Crearea unei instanțe de bucătărie
# bucatarie = Bucatarie('Bucatarie lui Ion')
#
# # Adăugarea de ingrediente
# bucatarie.adaugare_inventar('faina', 500)
# bucatarie.adaugare_inventar('oua', 6)
# bucatarie.adaugare_inventar('zahar', 200)
# bucatarie.adaugare_inventar('unt', 250)
#
# # Facerea unei rețete
# receta1 = {'faina': 200, 'oua': 2, 'zahar': 100, 'unt': 100}
# Bucatarie.fa_receta(receta1)  # Va afișa "Reteta '{'faina': 200, 'oua': 2, 'zahar': 100, 'unt': 100}' a fost realizata cu succes!"
# print(receta1)
# Verificarea cantității de ingrediente rămase

# print(bucatarie.ingrediente)  # Va afișa "{'f
# reteta2 = {'faina': 200, 'oua': 8, 'zahar': 100, 'unt': 100}
# bucatarie.fa_reteta(reteta2)  # Va afișa "Reteta '{'faina':

        # if self.inventar.get(nume_ingredient):
        #     self.inventar[nume_ingredient] -= cantitate
        # else:
        #     self.inventar[nume_ingredient] = cantitate
        # return self.inventar

# class Reteta(Bucatarie):
#
#     def __init__(self, nume, inventar):
#         super().__init__(nume)
#         self.inventar = inventar
#         self.lista_ingredientelor = inventar
#         self.cantitatea_ingredientului = 0
#     def ingredientul_folosit(self, numele, lista_ingredientelor, cantitatea_ingredientului):
#      if Bucatarie.get():
#     def __str__(self):
#         print(f'Inventar'{self.inventar})
#
#
#
# x = Bucatarie('Bucataria lui Ion')
# x.adaugare_inventar('rosii', 10)
#
# print(x.adaugare_inventar("sare", 20))
# print(x.adaugare_inventar("sare", 30))
# print(x.adaugare_inventar("sare", 30))
#
# print(x.scadere_inventar("sare", 30))
#
# y = Reteta.('rosii')
#
# print(y)
#