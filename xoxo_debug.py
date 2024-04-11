def is_legal(state):
    global legality
    o = state.count("O")
    x = state.count("X")
    if o - x >= 2 or x - o >= 2:
        legality = False
        return legality
    else:
        legality = True
        return legality

def winstate(rows, columns, diags):
    global legality
    global winrar
    dumbass = []
    for i in rows:
        if i[0] == i[1] == i[2] != "_":
            dumbass.append(i[0])
    for i in columns:
        if i[0] == i[1] == i[2] != "_":
            dumbass.append(i[0])
    for i in diags:
            if i[0] == i[1] != "_":
                dumbass.append(i[0])
    if "X" in dumbass and "O" in dumbass:
        print(dumbass)
        legality = False
        return legality
    elif len(dumbass) == 0:
        winrar = False
        return winrar
    else:
        winrar = True
        print(f'{dumbass[0]} wins!')
        return winrar
            
def is_finished(state):
    global finished
    if state.count("_") >= 1:
        finished = False
        return finished
    else:
        finished = True
        return finished


game = input()
matrix = [[x for x in game[:3]], [x for x in game[3:6]], [x for x in game[6:]]]
matrix_columns = [[x for x in game[0::3]], [x for x in game[1::3]], [x for x in game[2::3]]]
diagonals = [[x for x in game[0::4]], [x for x in game[2:7:2]]]

print("---------")
print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
print("---------")

is_legal(game)
if legality is False:
    print("Impossible1")
else:
    winstate(matrix, matrix_columns, diagonals)
    if legality is False:
        print("Impossible2")
    elif winrar is False:
        finished(game)
        if finished is True:
            print("Draw!!")
        elif finished is False:
            print("Game not finished")