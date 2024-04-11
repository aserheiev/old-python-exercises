number_row = [int(i) for i in input().split()]
find_num = int(input())
output = []
if find_num in number_row:
    for a, b in enumerate(number_row):
        if b == find_num:
            output.append(str(a))
    print(" ".join(output))
else:
    print("not found")