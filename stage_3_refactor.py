def get_matrix(game):
    matrix = [[x for x in game[:3]], [x for x in game[3:6]], [x for x in game[6:]]]
    matrix_columns = [[x for x in game[0::3]], [x for x in game[1::3]], [x for x in game[2::3]]]
    diagonals = [[x for x in game[0::4]], [x for x in game[2:7:2]]]
    return matrix, matrix_columns, diagonals


def print_state(matrix):
    print("---------")
    print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
    print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
    print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
    print("---------")
  

def is_legal(game, state):
    flat = "".join(item for row in state for item in row)
    o = game.count("O")
    x = game.count("X")
    if o - x >= 2 or x - o >= 2:
        return False
    elif "XXX" in flat and "OOO" in flat:
        return False
    return True


def winstate(game):
    rows, columns, diags = get_matrix(game)
    print_state(rows)
    state = rows + columns + diags
    dumbass = []
    for i in rows:
        if i[0] == i[1] == i[2] != "_":
            dumbass.append(i[0])
    for i in columns:
        if i[0] == i[1] == i[2] != "_":
            dumbass.append(i[0])
    for i in diags:
            if i[0] == i[1] == i[2] != "_":
                dumbass.append(i[0])
    if not is_legal(game, state):
        return "Impossible"
    if len(dumbass) == 0:
        if is_finished(game):
            return "Draw"
        return "Game not finished"
    else:
        return f'{dumbass[0]} wins'
 
           
def is_finished(state):
    return not state.count("_") >= 1


game = input("Enter cells:")   
state = winstate(game)
print(state)