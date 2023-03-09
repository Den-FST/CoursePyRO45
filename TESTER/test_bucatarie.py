import pytest

from bucatarie import Bucatarie

class TestBucatarie:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.nume = 'Bucataria lui Alexandru'
        self.bucatarie_test = Bucatarie(self.nume)

    def test_creare_obiect_bucatarie(self):

        assert self.bucatarie_test.nume == self.nume
        assert self.bucatarie_test.ingrediente == {}
        assert isinstance(self.bucatarie_test.ingrediente, dict) is True

    def test_adaugare_ingredient_inventar(self):
        nume_ingredient = 'ceapa'
        cantitate = 15
        self.bucatarie_test.adauga_ingredient(nume_ingredient, cantitate)
        assert self.bucatarie_test.ingrediente[nume_ingredient] == cantitate
    def test_fa_receta(self):
        salata_de_cartofi = {'ceapa': 200, 'cartofi': 50}
        self.bucatarie_test.adauga_ingredient('ceapa', 200)
        self.bucatarie_test.adauga_ingredient('cartofi', 50)
        assert self.bucatarie_test.ingrediente['ceapa'] >= 200
        assert self.bucatarie_test.ingrediente['cartofi'] >= 50
        resultat_reteta = self.bucatarie_test.fa_reteta(salata_de_cartofi)
        assert  resultat_reteta == True
        assert self.bucatarie_test.ingrediente['ceapa'] == 0
        assert self.bucatarie_test.ingrediente['cartofi'] == 0







