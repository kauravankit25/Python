def check(st):
    vowels = 'aeiou'
    for x in vowels:
        if x not in st.lower():
            return False
    return True


str1 = 'ABeeIghiObhkUul'
print(check(str1))