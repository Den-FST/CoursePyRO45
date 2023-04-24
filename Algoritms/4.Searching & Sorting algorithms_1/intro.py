"Write a function which will sort an array of numbers"
from typing import List
from functools import reduce

"Write an algorithm to sort the numbers"
a = [4,7,9,1,2,5,8,0]

def sort_array():
    for step in range(len(a)):
        min_index=step
        for index_array in range(step+1,len(a)):
            if a[min_index] > a[index_array]:
                min_index = index_array
        a[step], a[min_index] = a[min_index], a[step]
        print(a)


a=[2,3,1,5]
a=[2,1,3,5]

def bubble_sort(a):
    sortat = True
    for step in range(len(a)):
        for index in range(len(a)-step-1):
            if a[index] > a[index+1]:
                sortat = False
                a[index], a[index+1]= a[index+1], a[index]
        if sortat == True:
            return

# algoritm imbunatatit
# space = O(3)
# time best = O((len(a)-1)*1 = O(len(a))
# average = O(n^2)
# worst = O(n^2)

# space = O(2)
# time = O(len(a)*(len(a)-1)) = O(len(a)^2)


a=[4,7,9,1,2,5,0]
# a=[0,7,9,1,2,5,4]
# a=[0,1,9,7,2,5,4]
def sort_array(a):
    for step in range(len(a)):
        min_index=step
        for index_array in range(step+1,len(a)):
            if a[min_index]>a[index_array]:
                min_index=index_array
        a[step], a[min_index] =a[min_index], a[step]
        print(a)

#time complex O(len(a)*(len(a)-1))=O(len(a)^2)
# best case O(n^2)
# average case O(n^2)
# worst case O(n^2)

# space complex O(3)

"Write a function which will search for a specific element in an array"
def find_elem(a: List[int], elem) -> int:
    pass


"Write a function which will search for an element in a sorted  array"
def find_elem_sorted(a: List[int], elem) -> int:
    pass

"Write a function which will take a sorted array and which " \
"tell the position where  to insert 'elem'  in order to keep a SORTED"
def my_bisect(a: List[int], elem) -> int:
    pass


"We have a system that print on each day: '1' if system is valid, and '0' if system is invalid  "
"Initialy the system is valid. Print the day on which the system is invalidated" \
"Ex 1,1,1,1,0,0,0,0 , in this case algo should return 5"
def find_day(a: List[int], elem) -> int:
    pass


'''
Read about bisect function in python.
https://python.en.sdacademy.pro/coursebook/algorithms_and_data_structures/binary_search/
1. solve find_elem_sorted with bisect library
1.solve my_bisect function with bisect library
'''




if __name__ == "__main__":
    # sort_array()
