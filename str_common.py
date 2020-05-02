def counts(str1, str2):
    f = 0
    for x in str1:
        if str2.count(x) > 0:
            f += 1
    return f


# driven code
s1 = 'abcdef'  # first string
s2 = 'defghia'  # second string

# call count function
print(counts(s1, s2))