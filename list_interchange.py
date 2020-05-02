def change1(arr):
    # takes an array and
    # swap first and last element
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


def change2(arr):
    a, *c, d = arr
    arr = [d, *c, a]
    return arr


# driver code
a = [15, 12, 13, 10, 77, 54, 63]
print(change1(a))
print(change2(a))
del a[3:]
print(a)