def get_matrix():  #makes the grid
    game = "_________"
    matrix = [[x for x in game[:3]], [x for x in game[3:6]], [x for x in game[6:]]]
    return matrix

def print_game():  #prints the game grid in its current state
    print("---------")
    print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
    print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
    print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
    print("---------")

# checks if the inputs are valid and returns the coordinates
def valid_turn():
    while True:
        try:
            coords = (input("Please input two numbers from 1 to 3 separated by a space.\n>").split())
            if (coords[0].isnumeric() is False) or (coords[1].isnumeric() is False):
                print("Please input numbers only.")
                continue
        except IndexError:
            print("You entered only one number.")
            continue
        
        if (len(coords) > 2) or (len(coords) < 2):
            print("You entered either too few or too many numbers.")
            continue

        coords = [int(i) for i in coords]
        if (coords[0] >= 4 or coords[0] <= 0) or (coords[1] >= 4 or coords[1] <= 0):
            print("Coordinates should be from 1 to 3!")
            continue

        if matrix[(coords[0] - 1)][(coords[1] - 1)] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            break
    return coords

# grabs the coordinates, places the letter, calls the win condition check function and advances turn
def make_turn():
    global current_turn  #used to determine if it's X or Y turn
    coords = valid_turn()
    if current_turn % 2 != 0:
        matrix[(coords[0] - 1)][(coords[1] - 1)] = "X"
        print_game()
    elif current_turn % 2 == 0:
        matrix[(coords[0] - 1)][(coords[1] - 1)] = "O"
        print_game()
    if not is_finished():
        current_turn += 1
        make_turn()      

# runs a check if the game is won and returns boolean winstate value
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
    combos = columns + rows + diags  #collapses all the eligible lines into a single string for win condition checking
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
matrix = get_matrix()
print('Welcome to tic-tac-toe! Please input your moves as two numbers on a coordinate grid (e.g. "1 3") separated by a space.')
print_game()
make_turn()