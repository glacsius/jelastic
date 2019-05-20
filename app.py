from flask import Flask, Blueprint
from api.apirestplus import api
from api.namespace_register import add_namespaces

app = Flask(__name__)


def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    add_namespaces()
    flask_app.register_blueprint(blueprint)


def configure_app(flask_app):
    # flask_app.config['JSON_AS_ASCII'] = False  # config para utf-8 no jsonif
    pass


if __name__ == '__main__':
    configure_app(app)
    initialize_app(app)
    app.run(debug=True, host='0.0.0.0')


# HTTP Status
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
# https://nfe.io/doc/rest-api/nfe-v1/
