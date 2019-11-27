from flask import Blueprint, request, abort, Response

from .Connect4 import winning_move, validate_board

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


