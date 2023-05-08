# 12| 2 -> 0
# 6 | 2 -> 0
# 3 | 2 -> 1
# 1 | 2 -> 1
# 0
#
# 12 - 1100

# def conversie():
#     d = int(input())
#     result = []
#     while True:
#         if d >= 0:
#             r = d % 2
#             if r == 1:
#                 result.insert(0, "1")
#             else:
#                 result.insert(0, "0")
#             d = d // 2
#         if d == 0:
#             return "".join(result)


def conversie(d, b):
    if d != 0:
        conversie(d//b, b)
        print(d % b, end=" ")






if __name__ == '__main__':
    conversie(12, 2)


