def isprime(n):
    if n == 0 or n == 1:
        return False

    elif n == 2:
        return True

    else:
        for y in range(3, n):
            if n % y == 0:
                return False


        return True


def prime(L, H):
    count = []
    for x in range(L, H):
        if isprime(x):
            count.append(x)
    return count


low = int(input("Enter lower limit:"))
up = int(input("Enter upper limit:"))
total = prime(low, up)
print(f"Total primes between {low} and {up}: {len(total)}")
print("All prime:")
for x in total:
    print(x)