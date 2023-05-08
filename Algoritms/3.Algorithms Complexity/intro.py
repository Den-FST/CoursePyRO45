'''
Calculate the time and space complexity of following algorithm
'''


def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)

# suma(5) -> suma(4) -> suma(3) -> ... -> suma(0) -> O(n)
# time -> O(3*n+1) -> O(n)

'''
Calculate the time and space complexity of following algorithm
'''

# space -> O(1)
# time -> O(n)
def pair_sum_sequence(n):
    sum = 0
    for i in range(n):
        sum += pair_sum(i, i + 1)
    return sum


# SPace->O(1)
def pair_sum(a, b):
    return a + b


"""write an algo which calculate the sum and product of all elements
of an array (hint: use loop) and prints it out, also calculate the time/space complexity"""


def suma_produs(a):
    pass


"""Write a function which prints
    the  Cartesian Product of an array, also calculate space/time complexity"""


def produs_cartezian(a):
    pass


"""
use the logic from function produs_cartezian(a) and print only unordered pairs
calculate time/space complexity
"""


def print_unordered_list(a):
    pass


"""
write a function which will print all pairs of number of two different arrays.
calculate time/space complexity
"""


def print_pairs(a, b):
    pass


"""
From following which are equivalent to O(N), explain why?
O(N + P), where P > N
O(N + P), where P < N
O(5N)
O(N + NlogN)
O( N + logN)
O(N + M)
O(N * M)
"""


"""Discussion about  time complexity of fibbonaci recursive function"""
# fib(n) = fib(n-1) + fib(n-2)


"""What about fibbonaci with memoization"""

"""Discussion about time complexity in case of logN"""





if __name__ == '__main__':
    pass
