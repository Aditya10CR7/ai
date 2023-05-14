# minimax
import math

def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -10 + depth, None
    elif check_win(board, 'O'):
        return 10 - depth, None
    elif check_tie(board):
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for move in get_available_moves(board):
            board[move] = 'O'
            score, _ = minimax(board, depth + 1, False)
            board[move] = '-'
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for move in get_available_moves(board):
            board[move] = 'X'
            score, _ = minimax(board, depth + 1, True)
            board[move] = '-'
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def check_win(board, player):
    win_states = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    for state in win_states:
        if state == [player, player, player]:
            return True
    return False

def check_tie(board):
    return '-' not in board

def get_available_moves(board):
    return [i for i in range(len(board)) if board[i] == '-']

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])

board = ['-'] * 9
print_board(board)

while True:
    _, move = minimax(board, 0, True)
    board[move] = 'O'
    print_board(board)
    if check_win(board, 'O'):
        print('O wins!')
        break
    elif check_tie(board):
        print('Tie!')
        break

    move = int(input('Enter move: '))
    board[move] = 'X'
    print_board(board)
    if check_win(board, 'X'):
        print('X wins!')
        break
    elif check_tie(board):
        print('Tie!')
        break
    
    
# ------------------------------------------------------------------------------------------------
# import math

# def minimax(board, depth, is_maximizing):
#     # Base case: check for terminal state
#     winner = check_winner(board)
#     if winner is not None:
#         if winner == 'X':
#             return -10 + depth, None
#         elif winner == 'O':
#             return 10 - depth, None
#         else:  # Tie
#             return 0, None

#     if is_maximizing:
#         best_score = -math.inf
#         best_move = None
#         for move in get_empty_cells(board):
#             board[move[0]][move[1]] = 'O'
#             score, _ = minimax(board, depth + 1, False)
#             board[move[0]][move[1]] = ''
#             if score > best_score:
#                 best_score = score
#                 best_move = move
#     else:  # Minimizing player
#         best_score = math.inf
#         best_move = None
#         for move in get_empty_cells(board):
#             board[move[0]][move[1]] = 'X'
#             score, _ = minimax(board, depth + 1, True)
#             board[move[0]][move[1]] = ''
#             if score < best_score:
#                 best_score = score
#                 best_move = move

#     return best_score, best_move


# def get_empty_cells(board):
#     empty_cells = []
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == '':
#                 empty_cells.append((i, j))
#     return empty_cells


# def check_winner(board):
#     # Check rows
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] != '':
#             return board[i][0]

#     # Check columns
#     for j in range(3):
#         if board[0][j] == board[1][j] == board[2][j] != '':
#             return board[0][j]

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] != '':
#         return board[0][0]
#     elif board[0][2] == board[1][1] == board[2][0] != '':
#         return board[0][2]

#     # Check for tie
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == '':
#                 return None
#     return 'Tie'


# # Example usage:
# board = [['', '', ''], ['', 'O', 'X'], ['', '', 'X']]
# score, move = minimax(board, 0, True)
# print('Next optimal move:', move)

