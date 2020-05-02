import math


def is_perfect_square(x):
    # checks if the number is a perfect square or not
    s = int(math.sqrt(x))
    return s*s == x


def is_fibonacci(a):
    # checks if a number is fobonacci number or not
    # by calling the function is_perfect()

    return is_perfect_square(5*a*a+4) or is_perfect_square(5*a*a-4)


def fibo(n):
    # generates fibonacci series upto the number provided
    # and returns the list of all numbers in series
    a = [0, 1]
    for x in range(2, n):
        a.append(a[x-1]+a[x-2])
    return a


num = int(input("Enter number upto which series is to be printed:"))
print(fibo(num))
x = int(input("Enter number to check:"))
if is_fibonacci(x):
    print("Yes")
else:
    print("NO")