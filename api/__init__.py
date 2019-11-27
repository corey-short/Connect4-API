from flask import Flask

def create_app():
    app = Flask(__name__)

    from .BadRequestError import BadRequestError, bad_request

    @app.errorhandler(BadRequestError)
    def bad_request_handler(error):
        return bad_request(str(error))

    from .views import main
    app.register_blueprint(main)

    return app
