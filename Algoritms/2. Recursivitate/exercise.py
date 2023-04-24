# 1 find a recursive version of the function f(n) = 5*n (multiplii de 5)
from math import sqrt


def multiplu(n):
    if n == 0:
        return 1
    else:
        return 5 * multiplu(n-1)


# 2 write a recursive function that return the sum of the first n integers (similar to factorial)
def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)


# 3 write a function which calculates gcd(a,b) (adica cmmdc(a,b))
# hint algoritmul lui Euclid

    # while a != b:
    #     if a > b:
    #         a = a - b
    #     else:
    #         b = b - a
    # return a

def cmmdc(a, b):
    if a == b:
        return a
    elif a > b:
        return cmmdc(a-b,b)
    else:
        return cmmdc(b-a,a)

    # for i in range(2, sqrt(number) + 1):
    #     if number % i == 0:
    #         return False
    # return True

# 4 write a function which will calculate recursively all prime numbers untill n
prime_list = []
def prim_recursiv(n, i=2):
    # i = 2
    if  este_prim(i):
        prime_list.append(i)
    if i > n:
        return prime_list
    return prim_recursiv(n, i+1)



def este_prim(numar):
    if numar < 2:
        return False
    for i in range(2, int(sqrt(numar)) + 1):
        if numar % i == 0:
            return False
    return True



if __name__ == "__main__":
    # print(multiplu(10))
    # print(suma(10))
    print(cmmdc(10,35))
    print(prim_recursiv(99))
