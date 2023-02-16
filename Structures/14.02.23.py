from random import randint
# dict = {
#     "val" : 98,
#     57 : "text"
# }
#
# print(dict[57])
#
# dict[57] = 0
#
# for k,j in dict.items():
#     print(k)


# dict = {}
# list = [32, 87, 13, 25, 16, 88, 44, 55, 3, 10]
#
# for n in list:
#     if n % 2 == 0 :
#         key = list.index(n)
#         #dict.insert(key, n)
#         dict[key] = n
#
#
#
#
# print(dict)
#
# for index, numar in enumerate(list):
#     if numar % 2 == 0:
#         dict[index] = numar
# print(dict)

number = randint(0,100)
print(number)
i = 0

while True:
    inputmy = int(input())

    if inputmy < number:
        print('Incearca mai sus')
        i += 1
        #break
    elif inputmy > number:
        print('Incearca mai jos')
        i += 1
        #break
    else:
        print('Ai cistigat, numarul de incercari a fost {}'.format(i))
        break


