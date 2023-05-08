# a = [9,4,2,1,5]
# BUBBLE SORT
# a = [4,9,2,1,5]
# a = []
# a = []
# a = []

# INSERTION SORT
# a = [1,4,2,9,5]
# a = []

'''
SELECTION SORT
'''
def selection_sort(a):
    for step in range(len(a)):
        min_index=step
        for index_array in range(step+1,len(a)):
            if a[min_index] > a[index_array]:
                min_index=index_array
        a[step], a[min_index] =a[min_index], a[step]

'''
BUBBLE SORT
'''
def bubble_sort(a):
    sortat = True
    for step in range(len(a)):
        for index in range(len(a)-step-1):
            if a[index] > a[index+1]:
                sortat = False
                a[index], a[index+1]= a[index+1], a[index]
        if sortat == True:
            return


'''
BINARY SEARCH
'''
# def binary_search(a, elem):
#     st, fn = 0, len(a) - 1
#     while (st <= fn):
#         mid = (st + fn) // 2
#         if a[mid] == elem:
#             return mid
#         elif a[mid] > elem:
#             fn = mid - 1
#         else:
#             st = mid + 1


'''
BINARY SEARCH RECURSIVE
'''
"1,2,8,14,25"
def binary_search_recursive(a,st,fn, elem):
    pass




'''
INSERTION SORT

insertionSort(array)
  mark first element as selected -> nu il lua in urmatorul for
  for each unsorted element [ELEM]
    'extract' [ELEM]
    for j <- lastSortedIndex down to 0 -> can be replaced with a while loop
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
'''
def insertion_sort(a):
    pass

# 9,8,7,4,1
# WORST CASE -> O(N^2) -> array descrescator
# AVERAGE CASE -> O(N^2)
# 1,2,4,5,8
# BEST CASE -> O(N) -> array sortat crescator






'''QUICK SORT'''
def qs(a):
    pass







if __name__ == '__main__':
    pass