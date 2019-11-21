from flask import Blueprint, request, abort, Response

main = Blueprint('main', __name__)

@main.route('/evaluate_board_state', methods=['POST'])
def evaluate_board_state():
    boardstate_data = request.get_json()

    if validate_board(boardstate_data['board']) is False:
        return abort(400,'Not a standard gameboard size.')

    if winning_move(boardstate_data['board'], 1):
        return 'Player 1 wins!', 200

    if winning_move(boardstate_data['board'], 2):
        return 'Player 2 wins!', 200

    return 'Player, make next move', 200

def validate_board(board):
    if len(board) != 6 or len(board[0]) != 7:
        return False
    return True

def winning_move(board, piece):
    COLUMN_COUNT = 7
    ROW_COUNT = 6

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
