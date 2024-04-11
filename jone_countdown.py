while (a := int(input())) > 0:
    if a % 2 != 0 and a>1:
        a = a-1
    print(*[x for x in range(a, 0, -2)], sep='\n')