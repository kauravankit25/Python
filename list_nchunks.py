def chunks(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]


def check(arr):
    for i in range(0, len(arr), n):
        yield arr[i]*3


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(chunks(l, 4))
x = check(l)
print(x)
