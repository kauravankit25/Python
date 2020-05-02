def replace(arr, m):
    for x in range(0, len(arr)):
        if arr[x] > 0:
            arr[x+1] = (arr[x]+1) % m
            ar
    return arr
