from flask import Blueprint
from flask_restplus import Api, Resource


blueprint = Blueprint('cliente', __name__)
api = Api(blueprint, doc="/clientes_doc")

ns_cliente = api.namespace('clientes', description='Cadastro de clientes')


@ns_cliente.route('/')
class Clientes(Resource):
    def get(self):
        return 'Eu sou um clienteeee'
