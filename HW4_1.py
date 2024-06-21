import random
import time

# Board size
rows, cols = 9, 9

num_mines = 10
dx = [-1, -1, 0, 1, 1, 1, 0, -1] 
dy = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[' ' for j in range(cols)] for i in range(rows)]
mines = [[False for j in range(cols)] for i in range(rows)]
flags = [[False for j in range(cols)] for i in range(rows)]
revealed = [[False for j in range(cols)] for i in range(rows)]
mines_left = num_mines  #number of mines left to flag

def print_board():
    print('    a   b   c   d   e   f   g   h   i  ')
    print('  +' + '---+' * cols)
    for i in range(rows):
        row_str = f'{i+1} |'
        for j in range(cols):
            if not revealed[i][j] and not flags[i][j]:
                row_str += '   |'
            elif flags[i][j]:
                row_str += ' F |'   
            elif mines[i][j]:
                row_str += ' X |'  
            else:
                row_str += f' {count_nearby_mines(i, j)} |' 
        print(row_str)
        print('  +' + '---+' * cols)

def get_cell_value(x, y):
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return -1  
    elif mines[x][y]:
        return 9  
    elif not revealed[x][y]:
        return 0  
    else:
        return count_nearby_mines(x, y)  

def place_mines(first_x, first_y):
    mines_placed = 0
    while mines_placed < num_mines:
        x, y = random.randint(0, rows-1), random.randint(0, cols-1)
        if mines[x][y] or (x == first_x and y == first_y):
            continue
        elif abs(x - first_x) <= 1 and abs(y - first_y) <= 1:
            continue
        else:
            mines[x][y] = True
            mines_placed += 1

def count_nearby_mines(x, y):

    count = 0
    for i in range(8):
        if get_cell_value(x + dx[i], y + dy[i]) == 9:
            count += 1
    return count

def expand_empty_cells(x, y):

    if not revealed[x][y]:
        revealed[x][y] = True
        if count_nearby_mines(x, y) == 0:
            for i in range(8):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if not mines[new_x][new_y]:
                        expand_empty_cells(new_x, new_y)

def reveal_board():

    for i in range(rows):
        for j in range(cols):
            revealed[i][j] = True

def game_over():

    reveal_board()
    print_board()
    print('Game over')
    quit()

def check_win():

    for i in range(rows):
        for j in range(cols):
            if not revealed[i][j] and not mines[i][j]:
                return False
    return True

def play_game():

    start_time = time.time()
    print_board()
    while True:
        # Get user input
        user_input = input('Enter the cell ({} mines left): '.format(mines_left))
        if user_input == 'help':
            print("Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f)")
            continue
        elif len(user_input) < 2:
            continue
        cell_x, cell_y = ord(user_input[0]) - ord('a'), int(user_input[1:]) - 1


        if cell_x < 0 or cell_x >= rows or cell_y < 0 or cell_y >= cols:
            print('Invalid cell. Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f)')
            continue
        elif user_input.endswith('f'):
            flags[cell_x][cell_y] = not flags[cell_x][cell_y]
            print_board()
        elif mines[cell_x][cell_y]:
            game_over()
            break
        elif not revealed[cell_x][cell_y]:
            revealed[cell_x][cell_y] = True
            if count_nearby_mines(cell_x, cell_y) == 0:
                expand_empty_cells(cell_x, cell_y)
            print_board()
            if check_win():
                reveal_board()
                print_board()
                elapsed_time = time.time() - start_time
                print(f'You win. It took you {int(elapsed_time//60)} minutes and {int(elapsed_time%60)} seconds.')
                quit()

place_mines(0, 0)

play_game()
