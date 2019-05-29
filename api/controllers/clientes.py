from api import respostas
from api.modelos.clientes import ClienteModel
from database.db import add_obj, delete_obj
from functions.email import Email


class ClientesCtrl(object):

    def get(self, cnpj_cpf=None):

        if cnpj_cpf is None:
            return ClienteModel().query.all()
        else:
            res = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
            if res:
                return res
            else:
                return respostas.resp_notfound_404('Cliente')

    def post(self, request):
        cnpj_cpf = request.json.get('cnpj_cpf')
        res = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if res:
            return respostas.resp_registro_ja_existe_409('cliente', 'CNPJ/CPF')
        c = ClienteModel()
        c.cnpj_cpf = cnpj_cpf
        c.nome = request.json.get('nome')
        c.email_responsavel = request.json.get('email_responsavel')
        add_obj(c)
        return respostas.resp_post_created_201(c)

    def put(self, cnpj_cpf, request):
        c = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            c.nome = request.json.get('nome')
            c.email_responsavel = request.json.get('email_responsavel')
            add_obj(c)
            return respostas.resp_put_nocontent_204()
        else:
            return respostas.resp_notfound_404('Cliente')

    def delete(self, cnpj_cpf):
        c = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            delete_obj(c)
            return respostas.resp_delete_nocontent_204()
        else:
            return respostas.resp_notfound_404('Cliente')


class ClienteLiberadoCtrl(object):

    def get(self, cnpj_cpf):
        c = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            return respostas.resp_get_ok_200_obj({'liberado': str(c.autorizado)})
        else:
            return respostas.resp_notfound_404('Cliente')

    def put(self, cnpj_cpf, request):
        c = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            a = request.json.get('liberado')
            c.autorizado = a
            add_obj(c)
            return respostas.resp_put_nocontent_204()   # 204
        else:
            return respostas.resp_notfound_404('Cliente')


class ClienteSolicitarSenhaInstalacaoCtrl(object):
    MSG_EMAIL_ENVIADO_202 = 'E-email com a senha para instalação enviado'

    @staticmethod
    def __senha():
        return 'NT567'

    def post(self, cnpj_cpf, request):
        # request - devera vir o serial HD para podermos gerar a senha
        c = ClienteModel().query.filter_by(cnpj_cpf=cnpj_cpf).first()
        if c:
            email = c.email_responsavel
            cliente = c.cnpj_cpf + ' - ' + c.nome
            assunto = 'Envio de senha para instalação do Sistema AKS'
            html_body = '<h2>E-mail automático de solicitação de instalação do Sistema AKS</h2>'
            html_body += '<p>Empresa solicitante: ' + cliente
            html_body += '<center><p>Senha para instalação<p><b><font size="5">' + self.__senha()
            e = Email()
            res = e.enviar_email('suporte@akssistemas.com.br', email, assunto, html_body)
            if res:
                return respostas.resp_badrequest_erro_do_usuario_400('Erro ao enviar email: ' + res)
            else:
                return respostas.resp_post_accepted_202('E-mail enviado para ' + email)
        else:
            return respostas.resp_notfound_404('Cliente')


class ClienteValidarSenhaCtrl(object):
    MSG_VALIDAR_SENHA_202 = 'Senha válida'
    MSG_VALIDAR_SENHA_400 = 'Senha inválida'

    @staticmethod
    def __senha():
        return 'NT567'

    def post(self, request):
        try:
            senha_cliente = request.json.get('senha')
            # senha_cliente = request.json['senha']
        except KeyError as e:
            return {'message': 'Erro KeyError:'+str(e)}, 500
        except Exception as e:
            return {'message': 'Erro qualquer:' + str(e)}, 400

        if senha_cliente == self.__senha():
            return respostas.resp_post_accepted_202(self.MSG_VALIDAR_SENHA_202)
        else:
            return respostas.resp_badrequest_erro_do_usuario_400(self.MSG_VALIDAR_SENHA_400)
