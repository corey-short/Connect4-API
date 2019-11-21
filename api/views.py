from flask import Blueprint, request

main = Blueprint('main', __name__)

@main.route('/evaluate_board_state', methods=['POST'])
def evaluate_board_state():
    boardstate_data = request.get_json()

    return 'Done', 200

