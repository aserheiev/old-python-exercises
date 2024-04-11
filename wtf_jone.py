rang = int(input())
ind = [input() for i in range (rang)]
ind2 = [i.split(" ") for i in ind]
wincount = [sublist[1] for sublist in ind2 if sublist[1] == "win"]
print([sublist[0] for sublist in ind2 if sublist[1] == "win"])
print(wincount.count("win"))