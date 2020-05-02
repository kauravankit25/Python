def remove_duplicate(s):
    for x in s:
        if s.count(x) > 1:
            s = s.replace(x, '', 1)
    print(s)


str1 = "geeksforgeeks"
remove_duplicate(str1)