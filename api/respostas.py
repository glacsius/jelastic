from flask import jsonify
from werkzeug.exceptions import Conflict, NotFound, BadRequest


RESP_500_DOC = 'Erro no processamento no servidor'
RESP_409_DOC = 'Já existe um {} com o {} informado'
RESP_404_DOC = '{} não encontrado'
RESP_400_DOC = 'Algum parametro informado é inválido ou estrutura do JSON incorreto'
RESP_204_DOC_PUT = 'Registro alterado'
RESP_204_DOC_DEL = 'Registro excluído'
RESP_201_DOC_POST_CREATED = 'Registro adicionado'

# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/400


def resp_registro_ja_existe_409(nome_objeto, nome_campo: str):
    e = Conflict('My custom message')
    e.data = {'message': RESP_409_DOC.format(nome_objeto, nome_campo)}
    raise e


def resp_notfound_404(nome_objeto: str):
    e = NotFound('Não encontrado')
    e.data = {'message': RESP_404_DOC.format(nome_objeto)}
    raise e


def resp_badrequest_erro_do_usuario_400(mensagem: str):
    e = BadRequest('Não encontrado')
    e.data = {'message': mensagem}
    raise e


def resp_delete_nocontent_204():
    return {'message': RESP_204_DOC_DEL}, 204


def resp_put_nocontent_204():
    return {'message': RESP_204_DOC_PUT}, 204


def resp_post_accepted_202(mensagem):
    return {'message': mensagem}, 202


def resp_post_created_201(obj):
    return obj, 201


def resp_get_ok_200_obj(obj):
    return obj, 200


def resp_get_ok_200_msg(mensagem: str):
    resp = jsonify({'message': mensagem})
    resp.status_code = 200
    return resp

# ----------------------------------------------- Não utilizados

# MSG_INVALID_DATA = 'Ocorreu um erro nos campos informados.'
# MSG_DOES_NOT_EXIST = 'Este(a) {} não existe.'
# MSG_EXCEPTION = 'Ocorreu um erro no servidor. Contate o administrador.'
# MSG_ALREADY_EXISTS = 'Já existe um(a) {} com estes dados.'
#
# def resp_data_invalid(resource :str, errors: dict, msg: str = MSG_INVALID_DATA):
#     ''' Responses 422 Unprocessable Entity '''
#
#     if not isinstance(resource, str):
#         raise ValueError('O recurso precisa ser uma string.')
#     resp = jsonify({
#         'resource': resource,
#         'message': msg,
#         'errors': errors,
#     })
#     resp.status_code = 422
#     return resp
#
#
# def resp_exception(resource: str, description: str = '', msg: str = MSG_EXCEPTION):
#     # Responses 500
#
#     if not isinstance(resource, str):
#         raise ValueError('O recurso precisa ser uma string.')
#     resp = jsonify({
#         'resource': resource,
#         'message': msg,
#         'description': description
#     })
#     resp.status_code = 500
#     return resp
#
#
# def resp_does_not_exist(description: str):
#     # resp = jsonify({
#     #     'resource': resource,
#     #     'message': MSG_DOES_NOT_EXIST.format(description),
#     # })
#     # resp.status_code = 404
#     return {'message': description+' não encontrado'}, 404
#
#
# def resp_already_exists(resource: str, description: str):
#     # Responses 400
#
#     if not isinstance(resource, str):
#         raise ValueError('O recurso precisa ser uma string.')
#     resp = jsonify({
#         'resource': resource,
#         'message': MSG_ALREADY_EXISTS.format(description),
#     })
#     resp.status_code = 400
#     return resp
#
# def resp_ok_with_message(message: str, data=None, **extras):
#     # Responses 200
#
#     response = {'message': message}
#     if data:
#         response['data'] = data
#     response.update(extras)
#     resp = jsonify(response)
#     resp.status_code = 200
#     return resp
