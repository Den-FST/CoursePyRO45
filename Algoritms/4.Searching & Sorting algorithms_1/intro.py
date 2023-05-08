"Write a function which will sort an array of numbers"
from typing import List

"Write an algorithm to sort the numbers"
def sort_array(a):
    pass


"Write a function which will search for a specific element in an array"
def find_elem(a: List[int], elem) -> int:
    st, fn = 0, len(a)-1
    while(st<=fn):
        mid = (st+fn)//2
        if a[mid] == elem:
            return mid
        elif a[mid]> elem:
            fn = mid-1
        else:
            st = mid+1



"Write a function which will search for an element in a sorted  array"
def find_elem_sorted(a: List[int], elem) -> int:
    pass

"Write a function which will take a sorted array and which " \
"tell the position where  to insert 'elem'  in order to keep a SORTED"
def my_bisect(a: List[int], elem) -> int:
    st, fn = 0, len(a)
    while st < fn:
        mid = (st+fn) // 2
        if a[mid] <= elem:
            st = mid+1
        else:
            fn = mid
    return st




"We have a system that print on each day: '1' if system is valid, and '0' if system is invalid  "
"Initially the system is valid. Print the day on which the system is invalidated" \
"Ex 1,1,1,1,0,0,0,0 , in this case algo should return 5"
def find_day(a: List[int]) -> int:
    st, fn = 0, len(a)
    while(st<= fn):
        mid = (st+fn)//2
        if a[mid] == 1:
            if mid+1 < len(a) and a[mid+1] == 0:
                return mid+2
            st = mid+1
        else:
            fn = mid-1
    return -1


'''
Read about bisect function in python.
https://python.en.sdacademy.pro/coursebook/algorithms_and_data_structures/binary_search/
1. solve find_elem_sorted with bisect library
1.solve my_bisect function with bisect library
'''
import bisect
if __name__ == '__main__':
    pass
    a= [1,2,5,8,9,12,31]
    # print(my_bisect(a,31))
    # print(bisect.bisect_right(a,31))
    # print(bisect.bisect_left(a,31))
    print(find_elem(a,31))
    # a = [1,1,1,1,0,0,0]
    # print(find_day(a))