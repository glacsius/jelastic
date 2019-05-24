from database.db import db


class ClientesModel(db.Model):
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
