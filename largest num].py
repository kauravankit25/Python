def largest(arr):
    large = arr[0]
    for x in arr:
        if x>large:
            large = x
    return large


num = [15, 12, 13, 10]
print(largest(num))
