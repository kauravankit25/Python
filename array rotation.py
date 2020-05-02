def rotate(arr, n):

    return arr[n:] + arr[:n]


num = [15, 12, 13, 10, 77, 54, 63]
print(rotate(num, 2))
