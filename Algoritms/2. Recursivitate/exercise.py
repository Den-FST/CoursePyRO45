# 1 find a recursive version of the function f(n) = 5*n (multiplii de 5)
def multiplu(n):
    if n == 0:
        return 0
    if n == 1:
        return 5
    return 5 + multiplu(n-1)


# 2 write a recursive function that return the sum of the first n integers (similar to factorial)
def suma(n):
    if n == 0:
        return 0
    return n + suma(n-1)


# 3 write a function which calculates gcd(a,b) (adica cmmdc(a,b))
# hint algoritmul lui Euclid
def cmmdc(a, b):
    if b == 0:
        return a
    return cmmdc(b, a % b)


# 4 write a function which will calculate recursively all prime numbers untill n
# 16 - 3 , 5, 7 11 13
def prim_recursiv(n):
    pass

if __name__ == '__main__':
    # print(multiplu(7))
    # print(sum(range(10)) == suma(9))
    print(cmmdc(10,35))
