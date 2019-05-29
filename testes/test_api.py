import unittest
import json
from app import app, initialize_app
from flask import request
from api import respostas


class BasicTesteCase(unittest.TestCase):
    def setUp(self):
        initialize_app(app)
        # self.app = app
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_categoria_get(self):
        resp = self.client.get('/api/categories/')
        # print('Status code1', resp.status_code)
        # print('Data utf', resp.data.decode('utf-8'))
        assert 200 == resp.status_code

    def cliente(self):
        pass
        # response = self.client.get('/apis/clientes/')
        # self.assertEqual(200, response.status_code)
        # j = {
        #       "cnpj_cpf": "string",
        #       "nome": "string",
        #       "email_responsavel": "string"
        #     }
        # response = self.client.post('/api/clientes/', j)
        # assert 201 == response.status_code


    def request_args(self):
        with self.app.test_request_context('/sistemaaks/cnpjliberado/123'):
            self.assertEqual('glau', 'glau')

    def bd_vazio(self):
        print('Iniciando teste--------------------------------------------------')
        response = self.client.get('/sistemaaks/cnpjliberado/123')
        print(response.status_code)
        print(response.data)
        print(response.data.decode('utf-8'))
        with self.app.test_request_context('/sistemaaks/cnpjliberado/123'):
            print('Request.Path', request.path)
            print('Request.args', request.args)
            print('Request.Path', request.path)
        assert 'nenhuma entrada' != '12'

    def return_json(self):
        response = self.client.get('/sistemaaks/cnpjliberado/123')
        # data = json.loads(response.data.decode('utf-8'))
        # assert data['msg'] != 'world by apps'

    def seila(self):
        with app.test_request_context('/api/clientes'):
            app.preprocess_request()


class TestClientes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_all(self):
        response = self.client.get('/api/clientes')
        if response.status_code != 200:
            msg = response.json
            msg.update({'status_str': response.status})
        else:
            msg = ''
        self.assertEqual(200, response.status_code, msg)

    def test_get_unitario(self):
        # teata cnpj inexistente
        response = self.client.get('/api/clientes/00000')
        self.assertEqual(404, response.status_code)
        msg = respostas.RESP_404_DOC.format('Cliente')
        self.assertEqual(msg, response.json.get('message'))

        # testa ok
        response = self.client.get('/api/clientes/22161965840')
        self.assertEqual(200, response.status_code)

    def test_post(self):
        # testa o retorno 400 - erro faltando coisas
        response = self.client.post('/api/clientes', json={'nome': 'Testando legal'})
        self.assertEqual(400, response.status_code, response.json)
        erros = str(response.json)
        self.assertTrue('is a required property' in erros, response.json)

        # testa o retorno 201
        j = {
                "cnpj_cpf": "99999999",
                "nome": "Churros GLáucio é loção",
                "email_responsavel": "glaucio@pigarids.com.br"
        }
        response = self.client.post('/api/clientes', json=j)
        self.assertEqual(201, response.status_code, response.json)

        # testa o retorno 409 - já existe esse cnpj cadastrado
        response = self.client.post('/api/clientes', json=j)
        self.assertEqual(409, response.status_code, response.json)

        # testa alterar os dados 404 - com cnpj inexistente
        response = self.client.put('/api/clientes/7', json=j)
        self.assertEqual(404, response.status_code, response.json)
        msg = respostas.RESP_404_DOC.format('Cliente')
        self.assertEqual(msg, response.json.get('message'))

        # testa alterar os dados 400 - faltando informacao
        response = self.client.put('/api/clientes/'+j.get('cnpj_cpf'), json={'nome': 'Testando legal'})
        self.assertEqual(400, response.status_code, response.json)
        erros = str(response.json)
        self.assertTrue('is a required property' in erros, response.json)

        # testa alterar os dados 204 - tudo certo
        response = self.client.put('/api/clientes/'+j.get('cnpj_cpf'), json=j)
        if response.status_code != 204:
            erros = response.json
        self.assertEqual(204, response.status_code, erros)

        # testa excluir 404 - com cnpj inexistente
        response = self.client.delete('/api/clientes/7')
        self.assertEqual(404, response.status_code, response.json)
        msg = respostas.RESP_404_DOC.format('Cliente')
        self.assertEqual(msg, response.json.get('message'))

        # testa excluir 204 - tudo certo
        response = self.client.delete('/api/clientes/'+j.get('cnpj_cpf'))
        if response.status_code != 204:
            erros = response.json
        self.assertEqual(204, response.status_code, erros)

    def test_cliente_liberacao_get(self):
        # teata cnpj inexistente
        response = self.client.get('/api/clientes/00000/liberado')
        self.assertEqual(404, response.status_code)
        msg = respostas.RESP_404_DOC.format('Cliente')
        self.assertEqual(msg, response.json.get('message'))

        # testa ok
        response = self.client.get('/api/clientes/22161965840/liberado')
        self.assertEqual(200, response.status_code)
        resp = response.json.get('liberado')
        self.assertEqual(True, resp, response.json)

    def test_cliente_liberacao_put(self):
        # testa alterar os dados 404 - com cnpj inexistente
        response = self.client.put('/api/clientes/7/liberado', json={'liberado': True})
        self.assertEqual(404, response.status_code, response.json)
        msg = respostas.RESP_404_DOC.format('Cliente')
        self.assertEqual(msg, response.json.get('message'))

        # testa alterar os dados 400 - faltando informacao
        response = self.client.put('/api/clientes/22161965840/liberado', json={'lis': True})
        self.assertEqual(400, response.status_code, response.json)
        erros = str(response.json)
        self.assertTrue('is a required property' in erros, response.json)

        # testa alterar os dados 204 - tudo certo
        response = self.client.put('/api/clientes/22161965840/liberado', json={'liberado': True})
        if response.status_code != 204:
            erros = response.json
        self.assertEqual(204, response.status_code, erros)

    def test_cliente_solicitarSenhaInstalacao(self):
        # testa 404 - com cnpj inexistente
        response = self.client.post('/api/clientes/7/solicitar_senha_instalacao')
        self.assertEqual(404, response.status_code, response.json)
        msg = respostas.RESP_404_DOC.format('Cliente')
        self.assertEqual(msg, response.json.get('message'))

        # testa 202 - e
        response = self.client.post('/api/clientes/22161965840/solicitar_senha_instalacao')
        self.assertEqual(202, response.status_code, response.json)

    def test_cliente_validar_senha(self):
        # testa 400 - faltando informacao
        response = self.client.post('/api/clientes/validar_senha', json={'sen': '123'})
        self.assertEqual(400, response.status_code, response.json)
        erros = str(response.json)
        self.assertTrue('is a required property' in erros, response.json)

        # testa 202 - envio correto mas retornando senha inválida
        response = self.client.post('/api/clientes/validar_senha', json={'senha': '123'})
        self.assertEqual(400, response.status_code, response.json)
        erros = str(response.json)
        self.assertTrue('Senha inválida' in erros, response.json)




if __name__ == '__main__':
    unittest.main()
