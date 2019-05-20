from api.responses import resp_ok
from api.models.clientes_model import ClientesModel


class ClientesCtrl(object):

    def get(self, cnpj_cpf=None):
        if cnpj_cpf is None:
            return resp_ok({'msg': 'meu é gláucio'})
        else:
            return resp_ok({'msg': 'retorna só um'})


    def post(self, request):
        c = ClientesModel()
        c.cnpj_cpf = request.json.get('cnpj_cpf')
        c.nome = request.json.get('nome')
        return c
