def check(num):
    arm=0
    while num>0:
        arm = arm+(num%10)**3
        num=num//10

    return arm

x = int(input("Enter number:"))
print(check(x)==x)