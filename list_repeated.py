def remove_repeated(arr):
    duplicate = []
    for i in range(len(arr)):
        k = i+1
        for j in range(k, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicate:
                duplicate.append(arr[i])
    return duplicate


# driver code
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(remove_repeated(list1))