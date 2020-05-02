def increase(arr):
    if len(arr) == 1:
        return True
    else:
        flag = True
        for x in range(len(arr)-2):
            if arr[x]>arr[x+1]:
                flag = False
        return flag


def decrease(arr):
    if len(arr) == 1:
        return True
    else:
        flag = True
        for x in range(len(arr)-2):
            if arr[x]<arr[x+1]:
                flag = False
        return flag


a = [15, 12, 13, 10, 77, 54, 63]
a.sort()
print(increase(a) or decrease(a))