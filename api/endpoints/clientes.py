from flask import request
from flask_restplus import Resource, fields
from api.apirestplus import api
from api.controllers.clientes_ctrl import ClientesCtrl


ns = api.namespace('clientes', description='Operações dos clientes que utilizam o Sistema AKS')


clientes_serialize = api.model('clientes', {
    'cnpj_cpf': fields.String(required=True, description='CNPJ ou CPF do cliente'),
    'nome': fields.String(required=True, description='Nome do cliente - Fantasia + Razão Social')
})


@ns.route('/')
class ClientesList(Resource):

    @api.marshal_list_with(clientes_serialize)
    def get(self):
        return ClientesCtrl().get()

    @api.response(201, 'Cliente cadastrado')
    @api.response(400, 'Algum parametro informado é inválido')
    @api.response(409, 'Já existe um cliente com o CNPJ/CPF informado')
    @api.response(500, 'Erro no processamento')
    @api.expect(clientes_serialize)
    @api.marshal_with(clientes_serialize, code=201)
    def post(self):
        return ClientesCtrl().post(request), 201


@ns.route('/<cnpj_cpf>')
class Cliente(Resource):

    @api.marshal_with(clientes_serialize)
    def get(self, cnpj_cpf):
        return {'msg': 'meu teste'}

    @api.marshal_with(clientes_serialize)
    def put(self, cnpj_cpf):
        return 'nad'

    def delete(self, cnpj_cpf):
        return 'nad'
