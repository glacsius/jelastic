from flask import Flask, Blueprint
from api.apirestplus import api
from api.namespace_register import add_namespaces
from database.db import config_db

# ------------------------------------------------------------------------------------------
from flask import jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions, NotFound


class JSONExceptionHandler(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def std_handler(self, error):
        mensagem = error.description
        if 'The requested URL was not found on the server' in mensagem:
             mensagem = 'URL não existe'
        response = jsonify({'message': mensagem})
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response

    def init_app(self, app):
        self.app = app
        self.register(HTTPException)
        for code, v in default_exceptions.items():
            self.register(code)

    def register(self, exception_or_code, handler=None):
        self.app.errorhandler(exception_or_code)(handler or self.std_handler)


# ------------------------------------------------------------------------------------------


app = Flask(__name__)

# ------------------------------------------------------------------------------------------
handler = JSONExceptionHandler(app)

class UserNotFound(NotFound):
    def __init__(self, uid):
        super(UserNotFound, self).__init__()
        self.message = "Couldn't found a user with uid={}.".format(uid)

@app.route("/<int:uid>")
def home(uid):
    if uid != 0:
        raise UserNotFound(uid)
    else:
        return jsonify({'user': "Foo", "uid": 0})
# ------------------------------------------------------------------------------------------

def initialize_app(flask_app):
    __configure_app(flask_app)
    blueprints = Blueprint('apis', __name__, url_prefix='/api')
    api.init_app(blueprints)
    add_namespaces()
    flask_app.register_blueprint(blueprints)
    config_db(flask_app)


def __configure_app(flask_app):
    # flask_app.config['JSON_AS_ASCII'] = False  # config para utf-8 no jsonif
    app.config['RESTPLUS_VALIDATE'] = True  # padrao para validar todos os @api.expect
    app.config['ERROR_404_HELP'] = False  # para retirar mensagem q ele add ao enviar NotFound
    pass


if __name__ == '__main__':
    initialize_app(app)
    app.run(debug=True, host='0.0.0.0')


# HTTP Status
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
# https://nfe.io/doc/rest-api/nfe-v1/
