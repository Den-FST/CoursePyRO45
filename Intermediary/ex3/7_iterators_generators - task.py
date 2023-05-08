"""
### Iterators and Generators Task ###

###################
+   1. generate with normal iteration function first 100.000 numbers that can be divided by 7
+   2. do the same thing with an iteratior
+   3. do the same thing with a generator
+   4. measure the time for each option
###################


2. Control digit
	a. re-create point a, b, c from ex.1 but this time with control digit for first 100.000 numbers
	control digit = sum all digits of a number until you get 1 digit (ex: 476 => CD = 4+7+6 = 17 -> 1+7 = 8)


"""
import timeit




def digit_control(n):
    sum = 0

    while n > 0:
        c = n % 10
        sum += c
        n //= 10

        if sum > 9 and n == 0:
            n = sum
            sum = 0

    return sum



def normal_interation(n):
    i = 0
    ctrl_digit_list = []
    div_7_list = []

    for i in range(i, n+1):
        if i % 7 == 0:
            div_7_list.append(i)

    # for elem in div_7_list:
    #     total = 0
    #     while total > 9 :
    #         for char in str(elem):
    #             total += int(char)
    #             # print(total)
    #             # print(x + y)

    return print(f"Lista de numere divizibila cu 7: {div_7_list} ")

def is_div_7(n):
    if n % 7 == 0:
        return True

class div_7_iterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1

        if self.number >= self.n :
            raise StopIteration

        elif is_div_7(self.number):
            self.generated_numbers += 1
            return print(self.number)

        return self.__next__()

# class digicontrol_iterator:
#
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#
#         if self.number >= self.n :
#             raise StopIteration
#
#         elif digit_control(self.number):
#             self.generated_numbers += 1
#             return digit_control(self.number)
#
#         return self.__next__()


# class DigitControlIterator:
#
#     def __init__(self, n):
#         self.n = n
#         self.generated_numbers = 0
#         self.number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#
#         if self.generated_numbers >= self.n:
#             raise StopIteration
#
#         elif self.generated_numbers < self.n:
#             self.generated_numbers += 1
#             return digit_control(self.number)
#
#         return self.__next__()


def div_7_generator(n):

    number = 0
    generated_numbers = 0

    while number < n:

        if is_div_7(number):
            yield print(number)
            generated_numbers += 1

        number += 1




def generate_normal_option():
    print("-" * 50)
    print("NORMAL OPTION:")
    normal_interation(1000)
    print("\n\n")

def get_n_digit_control(n):

    print("NORMAL DIGI ITERATION:")
    digit_cont = []

    for x in range(1, n+1):
        digit_cont.append(digit_control(x))
    return print(digit_cont)

def digit_control_generator(n):

    number = 1
    generated_numbers = 0
    while generated_numbers < n:
        yield digit_control(number)
        generated_numbers += 1
        number += 1

def generate_iterator_option():
    print("-" * 50)
    print("ITERATOR OPTION:")
    div_7_list = div_7_iterator(100)
    i = 0
    for element in div_7_list:
        print(f"{element}   ---   {i}", end="\r")
        i += 1

    print("N primes generated!                     ")

    print("-" * 50)
    print("\n\n")

# def generate_iterator_digicontrol():
#     print("-" * 50)
#     print("ITERATOR OPTION Digi :")
#     div_7_list = digicontrol_iterator(100)
#     i = 0
#     for element in div_7_list:
#         print(f"{element}   ---   {i}", end="\r")
#         i += 1
#
#     print("N primes generated!                     ")
#
#     print("-" * 50)
#     print("\n\n")

def generate_generator_option():

    print("-" * 50)
    print("GENERATOR OPTION:")
    siv_7_no_generator = div_7_generator(100)
    i = 0
    for element in siv_7_no_generator:
        print(f"{element}   ---   {i}", end="\r")
        i += 1
    print("N primes generated!                     ")
    print("-" * 50)
    print("\n\n")

def generate_generator_digitcontrol():

    print("-" * 50)
    print("GENERATOR OPTION DIGICONTROL:")
    digi_control_list = digit_control_generator(10)
    # print(digi_control_list)     //for testing
    i = 0
    for element in digi_control_list:
        print(f"{element}   ---   {i}", end="\r")
        i += 1
    print("Generated!                     ")
    print("-" * 50)
    print("\n\n")




def main():
    generate_normal_option()
    generate_iterator_option()
    generate_generator_option()
    # generate_iterator_digicontrol()
    # get_n_digit_control(100)
    # digit_control_generator(100)
    # generate_generator_digitcontrol()

    # print("Please HIT ENTER to continue!")
    # input()

    setup_mode = ""
    code_normal = """
def normal_interation(n):
    i = 0
    div_7_list = []
    for i in range(i, n):
        if i % 7 == 0:
            div_7_list.append(i)
    return print(f"Lista de numere divizibila cu 7: {div_7_list}")
    """

    code_iterator = """
class div_7_iterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1

        if self.number >= self.n :
            raise StopIteration

        elif is_div_7(self.number):
            self.generated_numbers += 1
            return print(self.number)

        return self.__next__()

    """

    code_generator = """
def div_7_generator(n):

    number = 0
    generated_numbers = 0

    while number < n:

        if is_div_7(number):
            yield print(number)
            generated_numbers += 1

        number += 1
    """

    # print(f"normal: {timeit.timeit(stmt=code_normal, setup=setup_mode, number=100000)}")
    # print(f"iterator: {timeit.timeit(stmt=code_iterator, setup=setup_mode, number=100000)}")
    # print(f"generator: {timeit.timeit(stmt=code_generator, setup=setup_mode, number=100000)}")
    ###########################################################


if __name__ == "__main__":
    main()