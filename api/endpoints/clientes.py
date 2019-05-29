from flask import request
from flask_restplus import Resource
from api.apirestplus import api
from api.controllers.clientes import ClientesCtrl, ClienteLiberadoCtrl, ClienteSolicitarSenhaInstalacaoCtrl
from api.controllers.clientes import ClienteValidarSenhaCtrl
from api.modelos.clientes import cliente_restplus, cliente_liberacao, clientes_validar_senha
from api import respostas


ns = api.namespace('clientes', description='Clientes que utilizam o Sistema AKS')


@ns.route('')
class ClientesList(Resource):

    @api.response(500, respostas.RESP_500_DOC)
    @api.marshal_list_with(cliente_restplus, description='Retorno da lista de clientes')
    def get(self):
        '''Listar os clientes cadastrados'''
        return ClientesCtrl().get()

    @api.response(201, respostas.RESP_201_DOC_POST_CREATED)
    @api.response(400, respostas.RESP_400_DOC)
    @api.response(409, respostas.RESP_409_DOC.format('cliente', 'CNPJ/CPF'))
    @api.response(500, respostas.RESP_500_DOC)
    @api.marshal_with(cliente_restplus)
    @api.expect(cliente_restplus)
    def post(self):
        '''Criar um cliente'''
        return ClientesCtrl().post(request)


@ns.route('/<cnpj_cpf>')
class Cliente(Resource):

    @api.response(404, respostas.RESP_404_DOC.format('Cliente'))
    @api.response(500, respostas.RESP_500_DOC)
    @api.marshal_with(cliente_restplus)
    def get(self, cnpj_cpf):
        '''Obter um cliente'''
        return ClientesCtrl().get(cnpj_cpf)

    @api.response(204, respostas.RESP_204_DOC_PUT)
    @api.response(400, respostas.RESP_400_DOC)
    @api.response(404, respostas.RESP_404_DOC.format('Cliente'))
    @api.response(500, respostas.RESP_500_DOC)
    @api.expect(cliente_restplus)
    def put(self, cnpj_cpf):
        '''Atualizar um cliente'''
        return ClientesCtrl().put(cnpj_cpf, request)

    @api.response(204, respostas.RESP_204_DOC_DEL)
    @api.response(404, respostas.RESP_404_DOC.format('Cliente'))
    @api.response(500, respostas.RESP_500_DOC)
    def delete(self, cnpj_cpf):
        '''Excluir um cliente'''
        return ClientesCtrl().delete(cnpj_cpf)


@ns.route('/<cnpj_cpf>/liberado')
class ClienteLiberacao(Resource):

    @api.response(404, respostas.RESP_404_DOC.format('Cliente'))
    @api.response(500, respostas.RESP_500_DOC)
    @api.marshal_with(cliente_liberacao)
    def get(self, cnpj_cpf):
        '''Obter informação se o cliente está liberado para instalação/atualização'''
        return ClienteLiberadoCtrl().get(cnpj_cpf)

    @api.response(204, respostas.RESP_204_DOC_PUT)
    @api.response(400, respostas.RESP_400_DOC)
    @api.response(404, respostas.RESP_404_DOC.format('Cliente'))
    @api.response(500, respostas.RESP_500_DOC)
    @api.expect(cliente_liberacao)
    def put(self, cnpj_cpf):
        '''Atualizar liberação de instalação/atualização'''
        return ClienteLiberadoCtrl().put(cnpj_cpf, request)


@ns.route('/<cnpj_cpf>/solicitar_senha_instalacao')
class ClienteSolicitarSenhaInstalacao(Resource):

    @api.response(202, ClienteSolicitarSenhaInstalacaoCtrl().MSG_EMAIL_ENVIADO_202)
    @api.response(404, respostas.RESP_404_DOC.format('Cliente'))
    @api.response(500, respostas.RESP_500_DOC)
    def post(self, cnpj_cpf):
        '''Solicitar envio de email com a senha para instalação do Sistema AKS'''
        return ClienteSolicitarSenhaInstalacaoCtrl().post(cnpj_cpf, request)


@ns.route('/validar_senha')
class ClienteValidarSenha(Resource):

    @api.response(202, ClienteValidarSenhaCtrl().MSG_VALIDAR_SENHA_202)
    @api.response(400, respostas.RESP_400_DOC)
    @api.response(500, respostas.RESP_500_DOC)
    @api.expect(clientes_validar_senha)
    def post(self):
        '''Validar a senha de instalação'''
        return ClienteValidarSenhaCtrl().post(request)
