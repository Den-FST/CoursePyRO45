from simulare_calculator import adunare, scadere, inmultire, impartire
from simulare_calculator import simulare__calculator
import pytest


def test_adunare():
    a = 6
    b = 2

    asteptat = 8

    assert adunare(a, b) == asteptat


def test_scadere():

    a = 6
    b = 2

    asteptat = 4

    assert scadere(a, b) == asteptat


def test_inmultire():

    a = 6
    b = 2

    asteptat = 12

    assert inmultire(a, b) == asteptat


def test_impartire():

    a = 6
    b = 2

    asteptat = 3

    assert impartire(a, b) == asteptat


def test_simulare__calculator():
    x = 6
    y = 2
    z = "+"

    asteptat = 8

    assert simulare__calculator(x, y, z) == asteptat


def test_simulare__calculator_2():

    x = 6
    y = 2
    z = "-"

    asteptat = 4

    assert simulare__calculator(x, y, z) == asteptat


def test_simulare__calculator_3():

    x = 6
    y = 2
    z = "*"

    asteptat = 12

    assert simulare__calculator(x, y, z) == asteptat


def test_simulare__calculator_4():

    x = 6
    y = 2
    z = "/"

    asteptat = 3

    assert simulare__calculator(x, y, z) == asteptat


def test_simulare__calculator_impartire_la_zero():

    x = 6
    y = 0
    z = "/"

    with pytest.raises(ZeroDivisionError):
        simulare__calculator(x, y, z)
