def get_matrix():
    global matrix
    game = "_________"
    matrix = [[x for x in game[:3]], [x for x in game[3:6]], [x for x in game[6:]]]

def print_game():
    print("---------")
    print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
    print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
    print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
    print("---------")

def make_turn():
    global matrix
    global current_turn
    coords = (input("Make your turn...\n>").split())
    if (coords[0].isnumeric() is False) or (coords[1].isnumeric() is False):
        print("You should enter numbers!")
        make_turn()
    else:
        coords = [int(i) for i in coords]
        if (coords[0] >= 4 or coords[0] <= 0) or (coords[1] >= 4 or coords[1] <= 0):
            print("Coordinates should be from 1 to 3!")
            make_turn()
        elif matrix[(coords[0] - 1)][(coords[1] - 1)] != "_":
            print("This cell is occupied! Choose another one!")
            make_turn()
        else:
            if current_turn % 2 != 0:
                matrix[(coords[0] - 1)][(coords[1] - 1)] = "X"
                print_game()
            elif current_turn % 2 == 0:
                matrix[(coords[0] - 1)][(coords[1] - 1)] = "O"
                print_game()
            if not is_finished():
                current_turn += 1
                make_turn()

def is_finished():
    columns = \
        [f'{matrix[0][0]}{matrix[0][1]}{matrix[0][2]}', \
        f'{matrix[1][0]}{matrix[1][1]}{matrix[1][2]}', \
        f'{matrix[2][0]}{matrix[2][1]}{matrix[2][2]}']
    rows = \
        [f'{matrix[0][0]}{matrix[1][0]}{matrix[2][0]}', \
        f'{matrix[0][1]}{matrix[1][1]}{matrix[2][1]}', \
        f'{matrix[0][2]}{matrix[1][2]}{matrix[2][2]}']
    diags = \
        [f'{matrix[0][0]}{matrix[1][1]}{matrix[2][2]}', \
        f'{matrix[0][2]}{matrix[1][1]}{matrix[2][0]}']
    combos = columns + rows + diags
    if any(i for i in combos if i == "XXX"):
        print("X wins")
        return True
    elif any(i for i in combos if i == "OOO"):
        print("O wins")
        return True
    elif (any(i for i in combos if "_" in i)):
        return False
    else:
        print("Draw")
        return True
        
current_turn = 1
get_matrix()
print_game()
make_turn()