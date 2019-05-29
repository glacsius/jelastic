from flask_restplus import fields
from api.apirestplus import api
from database.db import db


cliente_restplus = api.model('Cliente', {
    'cnpj_cpf': fields.String(required=True, description='CNPJ ou CPF do cliente', example='00000000000000'),
    'nome': fields.String(required=True, description='Nome do cliente - Fantasia + Razão Social'),
    'email_responsavel': fields.String(required=True, description='E-mail do responsável da empresa')
})

cliente_liberacao = api.model('Cliente_liberacao', {
    'liberado': fields.Boolean(required=True, description='Cliente liberado para instalação e atualizações')
})

clientes_validar_senha = api.model('Cliente_validar_senha', {
    'senha': fields.String(required=True)
})


class ClienteModel(db.Model):
    __tablename__ = 'CLIENTES'
    cnpj_cpf = db.Column('cnpjcpf', db.String(14), primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    autorizado = db.Column(db.Boolean, nullable=False)
    email_responsavel = db.Column('emailresp', db.String(120))

    def __init__(self):
        self.cnpj_cpf = ''
        self.nome = ''
        self.autorizado = False
        self.email_responsavel = ''
