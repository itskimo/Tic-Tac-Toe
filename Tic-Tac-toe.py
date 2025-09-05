from random import randrange

def display_board(board):
    print("+-------" * 3 + "+")
    for row in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print(f"|   {board[row][col]}   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        move = input("Enter your move: ")
        if not move.isdigit():
            print("Invalid input! Please enter a number.")
            continue
        num = int(move)
        if num < 1 or num > 9:
            print("Number must be between 1 and 9!")
            continue
        row = (num - 1) // 3
        col = (num - 1) % 3
        if board[row][col] in ['X', 'O']:
            print("This field is already occupied! Choose another.")
            continue
        board[row][col] = 'O'
        break

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Check rows
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        idx = randrange(len(free_fields))
        row, col = free_fields[idx]
        board[row][col] = 'X'

# Initialize the board
board = [[str(i + 3*j + 1) for i in range(3)] for j in range(3)]
board[1][1] = 'X'  # Computer's first move

# Main game loop
while True:
    display_board(board)
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        break
    free = make_list_of_free_fields(board)
    if not free:
        display_board(board)
        print("It's a tie!")
        break
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("Computer won!")
        break
    free = make_list_of_free_fields(board)
    if not free:
        display_board(board)
        print("It's a tie!")
        break

    
#                                                                                                                                          ~kimo                                                                                                                     