import pytest

from calculator import adunare, scadere, impartire, inmultire



resultat = 0

print('Introduceti doua numere: ')
a = int(input())
b = int(input())
print('Introduceti tipul de operatie "+,-,*,/"')
op = input()

# def test_adunare(a,b):
#     assert adunare(a, b) == resultat

if op == '+':
    resultat = adunare(a,b)
    # with pytest.raises(AttributeError):
    #     print(adunare(a,b))
    # test_adunare(a, b)

    print('Rezultat: ', resultat)
elif op == '-':
    resultat = scadere(a,b)

elif op == '*':
    resultat = inmultire(a,b)

elif op == '/':
    resultat = impartire(a,b)

else:
    print('Operator gresit!')




