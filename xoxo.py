import __test

grid = input()
gridlist = []
for i in grid:
    gridlist.append(i)
    gridlist.append(" ")
string2 = "".join(gridlist)
print("---------")
print(f'| {string2[:5]} |')
print(f'| {string2[6:11]} |')
print(f'| {string2[12:17]} |')
print("---------")
print(__name__)