# def bubble_sort(listt):
#     for i, num in enumerate(listt):
#         try:
#             if listt[i+1] < num:
#                 listt[i] = listt[i+1]
#                 listt[i+1] = num
#                 bubble_sort(listt)
#         except IndexError:
#             pass
#     return listt


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = a[l+i]

    for i in range(n2):
        R[i] = a[m+i+1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]:
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

    # return a


def merge_sort(a, l, r):
    if l < r:
        m = (r + l) // 2

        merge_sort(a, l, m)
        merge_sort(a, m+1, r)
        merge(a, l, m, r)

    return a

listt = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(listt))

print(merge_sort(listt, 0, len(listt)-1))