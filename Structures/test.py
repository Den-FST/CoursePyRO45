import re
list1 = '366058562030849490134388085'

# list.sort()
# print(list[0])
# # for n in list
# var = list1[::2]
# print(var)
lstout = []

str = ''
for n in range(len(list1)):

    if int(list1[n]) <5 and int(list1[n]) >=0:
        # lstout = lstout + '0'
        lstout.append('0')
    else:
        lstout.append('1')

print(str.join(lstout))


    # print(list1[n])
    # for list1[n]
    #     print(list1)

# for n in var:
#     lstout = []
#
#     if int(n) < 5 and n >0 :
#         lstout.append('0')
#     else:
#         lstout.append('1')
#     print(lstout)
#
#


