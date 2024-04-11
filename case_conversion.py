phrase = input()
output = []
for i in phrase:
    if i.islower() is False:
        i = i.lower()
        if output:
            output.append("_")
        output.append(i)
    else:
        output.append(i)
phrase = "".join(output)
print(phrase)
