def nfibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return nfibo(n-1) + nfibo(n-2)


def nmultiple(k,n):
    f1=0
    f2=1
    i=2
    count=1
    while i!=0:
        f3 = f1+f2
        f1=f2
        f2=f3
        if f2%k==0:
            if count==n:
                print(f2)
                return i
            else:
                count+=1
        i+=1

print(nmultiple(4,5))

print(nfibo(5))