line = input()

if line.count("I") >= 3:
    omegajank = 0
    index_i = 0
    while omegajank < 3:
        index_i = line.index("I", index_i + 1)
        omegajank += 1
    jankline = line[:(index_i + 1)]
    print("Game over")
    print(jankline.count("C"))

if line.count("I") < 3:
    print("You won")
    print(line.count("C"))