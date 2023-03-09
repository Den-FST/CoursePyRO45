
def alege_primul_nr():
    x = int(input("Alege primul numar "))
    return x


def alege_al_doilea_nr():
    x = int(input("Alege al doilea numar "))
    return x


def operatorul():
    x = str(input("Alege  operatorul "))
    return x


def adunare(a, b):
    return a+b


def scadere(a, b):
    return a-b


def inmultire(a, b):
    return a*b


def impartire(a, b):
    return a / b


def simulare__calculator(x, y, z):
    if (z == "+"):
        return adunare(x, y)
    if (z == "-"):
        return scadere(x, y)
    if (z == "*"):
        return inmultire(x, y)
    if (z == "/"):
        return impartire(x, y)

# test_simulare_calculator va ignora codu de mai jos


if __name__ == '__main__':

    x = alege_primul_nr()
    y = alege_al_doilea_nr()
    z = operatorul()

    print(simulare__calculator(x, y, z))
