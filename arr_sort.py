x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]


z = zip(y, x)
k = [a for _, a in sorted(z) ]
print(k)