import timeit
import cProfile


def arr_test(stop): # 5.22sec
    start = 0
    # stop = 10
    step = 1
    fiind = 999
    array = list(range(start, stop, step))

    for element in array:
        if element == fiind:
            # print(element)
            return element

def arr_test11(stop):
    start = 0
    # stop = 10
    step = 1
    fiind = 999
    array = list(range(start, stop, step))

    fnd = [element for element in array if element == fiind]
    return fnd

def arr_test1(stop): # 17.67sec
    start = 0
    # stop = 10
    step = 1

    array = list(range(start, stop, step))
    for index, element in enumerate(array):
        print("Index:", index, "Valoare:", element)

def arr_test2(stop): # 18.08sec
    start = 0
    # stop = 10
    step = 1

    array = list(range(start, stop, step))
    for index in range(len(array)):
        print("Index:", index, "Valoare:", array[index])

def arr_test_zip1(stop): #9.58 sec
    start = 0
    # stop = 10
    step = 1

    array1 = list(range(start, stop, step))
    array2 = list(range(start, stop, step))
    for element1, element2 in zip(array1, array2):
        print(element1, element2)

def arr_test_sq1(stop): #1.82 sec
    start = 0
    # stop = 10
    step = 1

    array = list(range(start, stop, step))
    squared_array = [element ** 2 for element in array]
    print(squared_array)

def arr_test_zip2(stop): # 0.84 sec, 1.78sec
    start = 0
    # stop = 10
    step = 1

    array = list(range(start, stop, step))
    even_array = [element for element in array]
    # even_array = [element for element in array if element % 2 == 0]
    print(even_array)




# -------->    TEST ZONE <--------


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

n = 1000
wrapped = wrapper(arr_test11, n)
execution_time = timeit.timeit(wrapped, number=1000)
print(f"Total execution time for arr_test11 1000 runs: {execution_time:.5f} seconds")

n = 1000 # 5.22sec
wrapped = wrapper(arr_test, n)
execution_time = timeit.timeit(wrapped, number=1000)
print(f"Total execution time for arr_test 1000 runs: {execution_time:.5f} seconds")

# n = 1000 # 17.67sec
# wrapped = wrapper(arr_test1, n)
# execution_time = timeit.timeit(wrapped, number=1000)
# print(f"Total execution time for 1000 runs: {execution_time:.5f} seconds")

# n = 1000 # 18.08sec
# wrapped = wrapper(arr_test2, n)
# execution_time = timeit.timeit(wrapped, number=1000)
# print(f"Total execution time for 1000 runs: {execution_time:.5f} seconds")

# n = 1000 #9.58 sec
# wrapped = wrapper(arr_test_zip1, n)
# execution_time = timeit.timeit(wrapped, number=1000)
# print(f"Total execution time for 1000 runs: {execution_time:.5f} seconds")

# n = 1000 #1.82 sec
# wrapped = wrapper(arr_test_sq1, n)
# execution_time = timeit.timeit(wrapped, number=1000)
# print(f"Total execution time for 1000 runs: {execution_time:.5f} seconds")

# n = 1000 # 0.84 sec
# wrapped = wrapper(arr_test_zip2, n)
# execution_time = timeit.timeit(wrapped, number=1000)
# print(f"Total execution time for 1000 runs: {execution_time:.5f} seconds")

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# n = 200
# print("Profiling factorial_iterative:")
# cProfile.run("factorial_iterative(n)")
#
# print("\nProfiling factorial_recursive:")
# cProfile.run("factorial_recursive(n)")


# -------->  END TEST ZONE <--------