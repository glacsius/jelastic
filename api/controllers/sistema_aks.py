from api.respostas import resp_delete_nocontent_204, resp_put_nocontent_204, resp_notfound_404
from database.db import add_obj, delete_obj, maior


class SistemaAksCtrl(object):

    def get_ultimas_atualizacoes(self, num_at):
        url_base = 'http://pigarids.myftp.org:81/sistemaaks/new/'
        res = []
        for arq in ArquivosModel().query.filter(ArquivosModel.num_at > num_at):
            res.append({'nome': arq.nome+'.zip', 'at': arq.num_at, 'url': url_base + arq.nome + '.zip'})
        return res

    def get_arquivos(self, nome=None):
        if nome is None:
            return ArquivosModel().query.all()
        else:
            return ArquivosModel().query.filter_by(nome=nome).first()

    MSG_POST_ARQUIVO_201 = 'mN'
    def post_arquivo(self, request):


        from functions.validacoes import validar_json
        resp = validar_json(request, SchemaSenha())
        if resp:
            return resp

        # verificar se rola substituir o @api.expect(arquivos_serialize) e @api.marshal_with(arquivos_serialize)
        # pelo result = schema.dump(album) para devolver os resultados em json

        ultimo_id = maior(ArquivosModel.id)
        ultimo_num_at = maior(ArquivosModel.num_at)

        c = ArquivosModel()
        c.id = ultimo_id + 1
        c.nome = request.json.get('nome')
        c.versao = request.json.get('versao')
        c.num_at = ultimo_num_at + 1
        add_obj(c)
        return c

    def put_arquivo(self, nome, request):
        c = ArquivosModel().query.filter_by(nome=nome).first()
        if c:
            ultimo_num_at = maior(ArquivosModel.num_at)
            c.num_at = ultimo_num_at + 1
            c.versao = request.json.get('versao')
            add_obj(c)
            return resp_put_nocontent_204()
        else:
            return resp_notfound_404('Arquivo')

    def delete_arquivo(self, nome):
        c = ArquivosModel().query.filter_by(nome=nome).first()
        if c:
            delete_obj(c)
            return resp_delete_nocontent_204()
        else:
            return resp_notfound_404('Arquivo')
