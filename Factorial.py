def factorial(num):
    return 1 if num==0 or num==1 else  num*factorial(num-1)
a = int(input("Enter number:"))
print(f"factorial= {factorial(a)}")