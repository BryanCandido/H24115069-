import random

def create_board():

    board = {}
    for i in range(30):
        if random.random() <= 0.5: 
            board[i] = 'P'
        else:
            board[i] = '_'
    return board

def roll_dice():

    return random.randint(1, 6)

def move_player(player, steps):

    player += steps
    return player

def print_board(board, player_a, player_b, dice_a, dice_b):

    for i in range(30):
        if i == player_a and i == player_b:
            print('X', end='')  # Both players are on the same square
        elif i == player_a:
            print('A' if board[i] == '_' else 'a', end='')  # Player A is on the square
        elif i == player_b:
            print('B' if board[i] == '_' else 'b', end='')  # Player B is on the square
        else:
            print('_', end='')  # Empty square
    print(f" (A: {dice_a}, B: {dice_b})")  # Print dice rolls

def play_game():
    board = create_board()
    player_a = 0
    player_b = 0

    while True:
        dice_a = roll_dice()
        dice_b = roll_dice()

        print_board(board, player_a, player_b, dice_a, dice_b)

        if player_a not in board or player_b not in board:
            break

        if board[player_a] == 'P' and board[player_b] == 'P':
            board[player_a] = 'x'
            board[player_b] = 'x'
        elif board[player_a] == 'P':
            board[player_a] = 'x'
        elif board[player_b] == 'P':
            board[player_b] = 'x'

        player_a = move_player(player_a, dice_a)
        player_b = move_player(player_b, dice_b)

        if player_a >= 29 and player_b >= 29:
            break

    if player_a >= 29 and player_b >= 29:
        print("\nBoth players win!\n")
    elif player_a >= 29:
        print("\nPlayer A wins!\n")
    elif player_b >= 29:
        print("\nPlayer B wins!\n")

    for i in range(30):
        if board[i] == 'P':
            print('P', end='') 
        else:
            print('_', end='') 
    print()

play_game()