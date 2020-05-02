from collections import Counter


def remove_occurrence(arr, ele, n):
    # takes an array and remove
    # nth occurrence a particular element
    count = 0
    for i in range(len(arr)-1):
        if arr[i] == ele:
            count += 1
        if count == n:
            arr.pop(i)
            print(arr)
            break
    if count == 0:
        print("Item not found")


def occurance(arr, ele):
    # takes an array and a element
    # and counts its occurrence
    count = 0
    for i in range(len(arr)-1):
        if arr[i] == ele:
            count += 1
    if count == 0:
        print("Item not fount")
    else:
        return count


# driver code
a = [15, 12, 15, 13, 10, 15, 77, 54, 63]
print(f"occurances of 15 are {occurance(a, 15)}")
remove_occurrence(a, 15, 3)
print(a.count(15))
print(Counter(a))

