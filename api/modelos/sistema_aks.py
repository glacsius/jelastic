from flask_restplus import fields
from api.apirestplus import api
from database.db import db


arquivos_serialize = api.model('arquivos_schema', {
    'nome': fields.String(required=True, description='Nome puro do executável sem a extenção'),
    'num_at': fields.Integer(description='Número da última atualização - sequencial para todos os executáveis'),
    'versao': fields.String(description='Versão atual do exectuável')
})


class ArquivosModel(db.Model):
    __tablename__ = 'ARQUIVOS_AKS'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    num_at = db.Column(db.String(120), unique=True, nullable=False)
    versao = db.Column(db.String(80))

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.num_at = 0
        self.versao = ''
