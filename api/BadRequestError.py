from flask import jsonify

class BadRequestError(ValueError):
    pass

def bad_request(message):
    response = jsonify({
        'code': 400,
        'message': 'Invalid board state. ' + message
    })
    response.status_code = 400
    return response
