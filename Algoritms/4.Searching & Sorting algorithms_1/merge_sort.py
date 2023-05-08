
def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = a[p: p+n1]
    R = a[q+1: q+1+n2]

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
# L = [4,5,8,9]
#  R = [1,2,3]
# a = [1,2,3,4,5,8,9]


def merge_sort(a, p, r):
    if p < r:
        q = (r + p) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)



if __name__ == '__main__':
    a= [92,21,4,5,321,13,3]
    merge_sort(a,0, len(a)-1)
    print(a)