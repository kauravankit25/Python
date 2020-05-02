def sum_squares(n):
    return (n*(n+1)*(2*n+1))/6


def sum_cubes(n):
    return (n**2)*((n+1)**2)/4


num = int(input("Enter number:"))
print(f"Sum of squares of numbers upto {num} is: {sum_squares(num)}")
print(f"Sum of cubes of numbers upto {num} is: {sum_cubes(num)}")