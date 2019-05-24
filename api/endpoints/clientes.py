from flask import request
from flask_restplus import Resource, fields
from api.apirestplus import api
from api.controllers.clientes_ctrl import ClientesCtrl


ns = api.namespace('clientes', description='Operações dos clientes que utilizam o Sistema AKS')


clientes_serialize = api.model('clientes', {
    'cnpj_cpf': fields.String(required=True, description='CNPJ ou CPF do cliente', help='CNPJ/CPF não pode ser vazio'),
    'nome': fields.String(required=True, description='Nome do cliente - Fantasia + Razão Social'),
    'email_responsavel': fields.String(description='E-mail do responsável da empresa')
})

clientes_liberacao = api.model('cliente_liberacao', {
    'liberado': fields.Boolean(required=True)
})

clientes_validar_senha = api.model('cliente_validar_senha', {
    'senha': fields.String(required=True)
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


@ns.route('/validar_senha')
class ClienteValidarSenha(Resource):

    @api.response(200, ClientesCtrl().MSG_VALIDAR_SENHA_200)
    @api.response(400, ClientesCtrl().MSG_VALIDAR_SENHA_400)
    def get(self):
        return ClientesCtrl().validar_senha(request)

    @api.response(200, ClientesCtrl().MSG_VALIDAR_SENHA_200)
    @api.response(400, ClientesCtrl().MSG_VALIDAR_SENHA_400)
    def post(self):
        return ClientesCtrl().validar_senha(request)


@ns.route('/<cnpj_cpf>')
class Cliente(Resource):

    @api.marshal_with(clientes_serialize)
    def get(self, cnpj_cpf):
        return ClientesCtrl().get(cnpj_cpf)

    @api.response(204, 'Cliente alterado')
    @api.response(404, 'Cliente não encontrado')
    @api.expect(clientes_serialize)
    def put(self, cnpj_cpf):
        return ClientesCtrl().put(cnpj_cpf, request)

    def delete(self, cnpj_cpf):
        return ClientesCtrl().delete(cnpj_cpf)


@ns.route('/<cnpj_cpf>/liberado')
class ClienteInfo(Resource):

    def get(self, cnpj_cpf):
        return ClientesCtrl().info(cnpj_cpf)

    @api.response(204, 'Cliente alterado')
    @api.response(404, 'Cliente não encontrado')
    @api.expect(clientes_liberacao)
    def put(self, cnpj_cpf):
        return ClientesCtrl().info_put(cnpj_cpf, request)


@ns.route('/<cnpj_cpf>/solicitar_senha_instalacao')
class ClienteSolicitarSenhaInstalacao(Resource):

    def post(self, cnpj_cpf):
        return ClientesCtrl().solicitar_instalacao(cnpj_cpf, request)
