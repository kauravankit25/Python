def check(n):
    f = 0
    while n!=0:
        f = f + (n%10)
        n = n // 10

    if f % 2 == 0:
        return 0
    else:
        return 1


def binary(num):
    biny = 0
    while num !=0:
        biny = biny * 10 + num % 2
        num = num // 2
    biny = str(biny)
    biny = biny[::-1]
    biny = int(biny)
    return biny


# driver code
x = int(input(" "))
lis = []
for a in range(x):
    ele = int(input())
    lis.append(ele)
for a in range(len(lis)):
    lis[a] = binary(lis[a])


for a in lis:
    print(check(a))
