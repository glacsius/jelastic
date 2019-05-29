from flask import request
from api.apirestplus import api
from flask_restplus import Resource
from api.controllers.sistema_aks import SistemaAksCtrl
from api import respostas


ns = api.namespace('sistema_aks', description='Operações ref a atualização do Sistema AKS')


@ns.route('/lista_atualizacao/<int:num_at>')
class ClientesList(Resource):

    def get(self, num_at):
        return SistemaAksCtrl().get_ultimas_atualizacoes(num_at)


@ns.route('/arquivos')
class ClientesList(Resource):

    @api.marshal_list_with(arquivos_serialize)
    def get(self):
        return SistemaAksCtrl().get_arquivos()

    @api.response(201, 'Cliente cadastrado')
    @api.response(400, 'Algum parametro informado é inválido')
    @api.response(409, 'Já existe um cliente com o CNPJ/CPF informado')
    @api.response(500, 'Erro no processamento')
    @api.expect(arquivos_serialize)
    #@api.marshal_with(arquivos_serialize, code=201)
    def post(self):
        return SistemaAksCtrl().post_arquivo(request)


@ns.route('/arquivos/<nome>')
class Cliente(Resource):

    @api.marshal_with(arquivos_serialize)
    def get(self, nome):
        return SistemaAksCtrl().get_arquivos(nome)

    @api.response(204, 'Arquivo alterado')
    @api.response(404, 'Arquivo não encontrado')
    @api.expect(arquivos_serialize)
    def put(self, nome):
        return SistemaAksCtrl().put_arquivo(nome, request)

    def delete(self, nome):
        return SistemaAksCtrl().delete_arquivo(nome)
