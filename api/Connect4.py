from .BadRequestError import BadRequestError

COLUMN_COUNT = 7
ROW_COUNT = 6

def validate_board(board):
    if not check_board_length(board):
        raise BadRequestError('Gameboard size must be 6 by 7.')
    if check_disconnected_pieces(board):
        raise BadRequestError('Pieces cannot be disconnected.')
    if not check_number_of_pieces(board):
        raise BadRequestError('Player has incorrect number of pieces on the board.')

def check_board_length(board):
    if len(board) != 6 or len(board[0]) != 7:
        return False
    return True

def check_number_of_pieces(board):
    player1Count = 0
    player2Count = 0
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                player1Count += 1
            if board[r][c] == 2:
                player2Count += 1

    if player2Count > player1Count or player1Count - player2Count > 1:
        return False
    return True

def check_disconnected_pieces(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 1):
            if board[r][c] != 0 and board[r+1][c] == 0:
                return True

def check_is_draw(board):
    pass

def winning_move(board, piece):
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positive slopes
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negative slopes
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
