from calculator import adunare, capitalizare


def test_adunare():
    a = 10
    b = 30
    asteptat = 40
    assert  adunare(a, b) == asteptat

def test_caitalizare():
    variabila = 'bucuresti'
    assert capitalizare(variabila) == 'Bucuresti'

# def returneaza_cel_mai_mare_numar_din_listaq(l):
#