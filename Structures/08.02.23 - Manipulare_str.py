import binascii



# string1 = 'Ovidiu are pere'
# print( string1[0])
# print( string1[2])
# print( len(string1), 23)
# print( string1.index('are'))
# print(string1.count('e'))


# for caracter in string1:
#     print(caracter)
#
# for c in "George":
#     print(c)

# string1 = 'Astazi este o zi frumoasa'
#
# # for n in string1:
# a = string1.count('a') + string1.count('A')
# e = string1.count('e') + string1.count('E')
# i = string1.count('i') + string1.count('I')
# o = string1.count('o') + string1.count('O')
# u = string1.count('u') + string1.count('U')
#
# print( 'a:', a ,  'e:' ,e ,  'i:', i,  'o:',o,  'u:',u )

#
#
# print( ord('a'))
# print(chr(97))
import string

# st = 'Ana are mere'.encode('utf-8')
# st.hex()
# print(st.hex())

# string1 = 't'
# ascii_string1 = ord(string1)
# ascii_string1 = ascii_string1 - 32
# print(ascii_string1)
# string1 = chr(ascii_string1)
# print(string1)

# str = 'O zi frumoasa'
# for n in str:
#     if ord(n) <= 122 and ord(n) >= 97:
#         print('Aceasta este o minuscola: {}'.format(n))


#caesar cypher

# lst = []
# d = 'Bna'
#
#
# for n in d:
#     n = ord(n) + 1
#     lst.append(chr(n))
# print(lst)
#
# for n in lst:
#     n = ord(n) - 1
#     lst.append(chr(n))
# print(lst)

# mesaj = "Ana"
#
# asci1 = ord(mesaj[0])
# asci2 = ord(mesaj[1])
# asci3 = ord(mesaj[2])
#
# # print(asci1)
# # print(asci2)
# # print(asci3)
#
# asci1 += 5
# asci2 += 5
# asci3 += 5
#
# mesaj_criptat = chr(asci1) + chr(asci2) + chr(asci3)
#
# print(mesaj)
# print(mesaj_criptat)
#
#
# #######
# asci1 = ord(mesaj_criptat[0])
# asci2 = ord(mesaj_criptat[1])
# asci3 = ord(mesaj_criptat[2])
#
# asci1 = asci1 -5
# asci2 = asci2 -5
# asci3 = asci3 -5
#
#
# mesaj = chr(asci1) + chr(asci2) + chr(asci3)
# print(mesaj)


# def cryptare(t):
#     str = ''
#     for n in t:
#         n = ord(n) + 5
#         n = chr(n)
#         str += n
#     return str
#
# def decryptare(t):
#     str = ''
#     for n in t:
#         n = ord(n) - 5
#         n = chr(n)
#         str += n
#     return str
#
# t = cryptare('text secret')
# print(t)
# t1 = decryptare(t)
# print(t1)


# for n in lst:
#     n = ord(n) - 1
#     lst.append(chr(n))
# print(lst)

# s1 = "ATTTTGCATTCTCGATTAGCATGCATGCAT"
# s2 = "ATTTTGCCTTCTCGATGAGCATGCACGCAT"
# i = 0
# total = 0
# for n in s1:
#     if s1[i] != s2[i]:
#         total += 1
#     i += 1
# print('Total diferente: {}'.format(total))
