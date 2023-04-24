### Iterators and Generators ###
"""
1. Normal
2. Iterators
3. Generators
"""
import timeit
from math import sqrt

def normal_iteration():

    #############################
    ### list ###
    print("List:")
    a = [1, 2, 3, 4]
    for item in a:
        print(item)
    print("\n\n")
    #############################

    #############################
    ### string ###
    print("String:")
    a = "Alice has a cat"
    for item in a:
        print(item)
    print("\n\n")
    #############################

    #############################
    ### dictionary ###
    print("Dictionary:")
    a = {'name': "Adam", 'surname': "Smith"}
    for key in a:
        print(f"{key}: {a[key]}")
    print("\n\n")
    #############################


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True



def get_n_primes(n):

    primes = []
    i = 2

    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
            if len(primes) % 1000 == 0:
                print(len(primes), end="\r")

        i += 1

    return primes


def generate_normal_option():

    print("-" * 50)

    # [2, 3, 5, 7, 11, 13, 17]
    prime_no_list = get_n_primes(5000)

    print(f"type: {type(prime_no_list)}")
    print(f"len(primes):{len(prime_no_list)}")
    i = 0
    for element in prime_no_list:
        i += 1
        print(f"{element} --- {i}", end="\r")  

    print("-" * 50)
    print("\n\n")


class NumerePrime:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self


    def __next__(self):

        self.number += 1

        if self.generated_numbers >= self.n:
            raise StopIteration

        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number

        return self.__next__()


def generate_iterator_option():
    print("-" * 50)

    prime_no_iterator = NumerePrime(5000)

    i = 0
    print(f"type: {type(prime_no_iterator)}")
    for element in prime_no_iterator:
        i += 1
        print(f"{element} --- {i}", end="\r")  

    print("-" * 50)
    print("\n\n")


def prime_generator(n):

    number = 2
    generated_numbers = 0

    while generated_numbers < n:

        if is_prime(number):
            yield number        ### se comporta ca un return ###
            generated_numbers += 1

        number += 1


def generate_generator_option():
    print("-" * 50)

    prime_no_generator = prime_generator(5000)

    i = 0 
    for element in prime_no_generator:
        i += 1
        print(f"{element} --- {i}", end="\r")  


    print("-" * 50)
    print("\n\n")


def main():

    # normal_iteration()
    
    ###########################################################
    ### generate N prime numbers ### normal option ###
    # generate_normal_option()
    ###########################################################

    # input("Please HIT ENTER to continue!")

    ###########################################################
    ### generate N prime numbers ### iterator ###
    # generate_iterator_option()
    ###########################################################

    # input("Please HIT ENTER to continue!")

    ###########################################################
    ### generate N prime numbers ### generator ###
    # generate_generator_option()
    ###########################################################


    ###########################################################
    ### process time ### timeit ###
        
    setup_mode = "from math import sqrt"
    code_normal = """
def get_n_primes(n):

    primes = []
    i = 2

    while len(primes) < n:

        if is_prime(i):
            primes.append(i)
        i += 1
    """

    code_iterator = """
class PrimeIterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1


    def __iter__(self):
        
        return self


    def __next__(self):
        
        self.number += 1
        
        if self.generated_numbers >= self.n:
            raise StopIteration

        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number

        return self.__next__()

    """

    code_generator = """
def generate_generator_option(n):

    number = 2
    generated_numbers = 0

    while generated_numbers < n:

        if is_prime(number):
            yield number
            generated_numbers += 1

        number += 1
    """

    print(f"normal: {timeit.timeit(stmt=code_normal, setup=setup_mode, number = 100000)}")
    print(f"iterator: {timeit.timeit(stmt=code_iterator, setup=setup_mode, number= 100000)}")
    print(f"generator: {timeit.timeit(stmt=code_generator, setup=setup_mode, number = 100000)}")
    ###########################################################

if __name__ == "__main__":
    main()