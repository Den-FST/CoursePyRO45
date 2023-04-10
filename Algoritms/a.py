# write a function which will take as input a number and output "YES" is number is odd and "NO"
# if number is even
import re
from typing import List


def even_or_odd(n):
    if n % 2 == 0:
        print(f'Numarul {n} este par')
    else:
        print(f'Numarul {n} este impar')


# scrieti o functie care primeste ca input un numar natural, si printeaza "Fizz" daca numarul este divizibil cu 5
# "Buzz" daca numarul este divizibil cu
def fizz_buzz(n):
    if n > 5:
        if n % 7 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Fizz")
        elif n % 7 == 0:
            print("Buzz")




# scrieti o functie care calculeaza factorialul numarului natural n (n! = n*(n-1)*(n-2)* ... * 1 , where 0! = 1)
def factorial(n: int):
    i = 0
    res = 1
    for i in range(1, n+1):
        res *= i
    print(f"Factorial de {n}! = {res}")



# scrieti o functie care determina daca numarul intreg n este sau nu prim
def prim(n):
    if n % 2 == 0:
        return print(f"Numarul {n} este prim")
    return print(f"Numarul {n} nu este prim")


def anagrame(word: str, list_of_words: List[str]) -> List[str]:

    sorted_word = ''.join(sorted(word))
    anagrams = []

    for w in list_of_words:
        sorted_w = ''.join(sorted(w))
        if sorted_word == sorted_w:
            anagrams.append(w)
    return anagrams



if __name__ == '__main__':
    n = int(input("Introdu un numar: ")) # input numarul
    even_or_odd(n)
    prim(n)          # verificam daca e prim
    fizz_buzz(n)     #daca se imparte la 5 fizz, daca la 7 buzz, daca la amandoua fizzbuzz
    factorial(n)

    anagrw = input("Introdu primult cuvint: ")
    l = []
    i=3
    a=i+1
    for i in range(0, i):
        a -= 1
        anagr = input(f"Adauga in lista de cuvinte inca {a} : ")
        l.append(anagr)

    print(anagrame(anagrw, l) )