inp = input()
list1 = [int(i) for i in inp]
list2 = []

for a, _b in enumerate(list1):
    if a == 0:
        pass
    list2.append(sum(list1[0:(a + 1):1]))
print(list2)