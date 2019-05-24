from api.responses import resp_delete_ok_204, resp_put_ok_204, resp_nao_encontrado_404, resp_ok_200, resp_invalido_400
from api.models.clientes_model import ClientesModel
from database.db import add_obj, delete_obj
from functions.email import Email


class ClientesCtrl(object):

    def get(self, cnpj_cpf=None):
        if cnpj_cpf is None:
            return ClientesModel().query.all()
        else:
            return ClientesModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()

    def post(self, request):
        c = ClientesModel()
        c.cnpj_cpf = request.json.get('cnpj_cpf')
        c.nome = request.json.get('nome')
        c.email_responsavel = request.json.get('email_responsavel')
        add_obj(c)
        return c

    def put(self, cnpj_cpf, request):
        c = ClientesModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            c.nome = request.json.get('nome')
            c.email_responsavel = request.json.get('email_responsavel')
            add_obj(c)
            return resp_put_ok_204()
        else:
            return resp_nao_encontrado_404('Cliente')

    def delete(self, cnpj_cpf):
        c = ClientesModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            delete_obj(c)
            return resp_delete_ok_204()
        else:
            return resp_nao_encontrado_404('Cliente')

    def info(self, cnpj_cpf):
        c = ClientesModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            return {'liberado': str(c.autorizado)}, 200
        else:
            return resp_nao_encontrado_404('Cliente')

    def info_put(self, cnpj_cpf, request):
        c = ClientesModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            a = request.json.get('autorizado')
            c.autorizado = a
            add_obj(c)
            return resp_put_ok_204()   # 204
        else:
            return resp_nao_encontrado_404('Cliente')

    def solicitar_instalacao(self, cnpj_cpf, request):
        c = ClientesModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        email = c.email_responsavel
        cliente = c.cnpj_cpf + ' - ' + c.nome
        assunto = 'Envio de senha para instalação do Sistema AKS'
        html_body = '<h2>E-mail automático de solicitação de instalação do Sistema AKS</h2>'
        html_body += '<p>Empresa solicitante: ' + cliente
        html_body += '<center><p>Senha para instalação<p><b><font size="5">' + self.__senha()
        e = Email()
        res = e.enviar_email('suporte@akssistemas.com.br', email, assunto, html_body)
        if res:
            return resp_ok_200('Erro ao enviar email: ' + res)
        else:
            return resp_ok_200('E-mail enviado para ' + email)

    def __senha(self):
        return 'NT567'

    MSG_VALIDAR_SENHA_200 = 'Senha válidada'
    MSG_VALIDAR_SENHA_400 = 'Senha inválida'

    def validar_senha(self, request):

        from marshmallow import Schema, fields as f
        class SchemaSenha(Schema):
            senha = f.String(required=True, error_messages={'required': 'O campo senha é requerido'})

        from functions.validacoes import validar_json
        resp = validar_json(request, SchemaSenha())
        if resp:
            return resp

        # resp = SchemaSenha().validate(j)
        # if resp:
        #     for erro in resp:
        #         return {'message': resp[erro][0]}

        try:
            # senha_cliente = request.json.get('senha')
            senha_cliente = request.json['senha']
        except KeyError as e:
            return {'message': 'Erro KeyError:'+str(e)}, 500
        except Exception as e:
            return {'message': 'Erro qualquer:' + str(e)}, 400

        if senha_cliente == self.__senha():
            return resp_ok_200(self.MSG_VALIDAR_SENHA_200)
        else:
            return resp_invalido_400(self.MSG_VALIDAR_SENHA_400)
