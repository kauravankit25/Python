from functools import reduce
import math


def largest(arr,n):
    arr = list(set(arr))
    arr.sort()
    a = arr[::-1]
    return a[:n]


list1 = [1, 5, 8, 9]
list2 = [3, 6, 3, 67, 54, 1, 0]
print(reduce(lambda x, y: x*y, list1))
print(math.prod(list2))
print(largest(list2, 5))


