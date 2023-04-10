"""
algoritm
input numar
in functie de paritate printeaza par sau impar
"""




"""
functie check_number:
input numar
if numar divizibil cu 2, print "par"
else print "impar"
"""


def check_number():
    x = input("Introdu numarul: ")

    if int(x) % 2 == 0:
        print('Numarul par')
    else:
        print('Numarul este inpar')


if __name__ == "__main__":
    check_number()
