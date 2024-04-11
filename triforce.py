size = int(input())
e = 1
for i in range(size):
    strang = "#" * e
    print(strang.center(size * 2))
    e += 2