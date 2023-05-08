# write a function which will take as input a number and output "YES" is number is odd and "NO"
# if number is even

from collections import Counter
from typing import List


# scrieti o functie care determina daca numarul intreg n este sau nu prim()
#  n - este prim daca e divizibil cu 1 si cu el insusi.
# 17 -> 3,4,...16  18 - 3
# 100 - 1, 2, 4, 5, 10, 20, 25,50, 100
def prim(n):
    flag = False
    if n % 2 == 0:
        flag = True
    if flag == False:
        for i in range(3, n):
            if n % i == 0:
                flag = True
                break
    if flag == True:
        print(f'{n} - Nu e prim!')
    else:
        print(f'{n} - e prim!')


# ion <-> noi
# <k:v>
def anagrame(word: str, list_of_words: List[str]) -> List[str]:
    dict_word = Counter(word)
    print(dict_word)
    result = []
    for cuvant in list_of_words:
        if Counter(cuvant) == dict_word:
            result.append(cuvant)
    return result


if __name__ == '__main__':
    list1 = range(0, 100)
    for elem in list1:
        prim(elem)
    # print(anagrame("ioon", ["noi", "nou"]))
