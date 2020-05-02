def remain(arr, n):
    # gets an array and a number
    # returns remainder of all
    # numbers multiplied at once

    mul = 1

    for x in arr:
        # not following direct approach
        # to avoid overflow

        mul = (mul * (x % n)) % n
    return mul % n


# driven code
a = [15, 12, 13, 10, 77, 54, 63]
print(remain(a, 17))
