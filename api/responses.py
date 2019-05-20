from flask import jsonify


MSG_INVALID_DATA = 'Ocorreu um erro nos campos informados.'
MSG_DOES_NOT_EXIST = 'Este(a) {} não existe.'
MSG_EXCEPTION = 'Ocorreu um erro no servidor. Contate o administrador.'
MSG_ALREADY_EXISTS = 'Já existe um(a) {} com estes dados.'


def resp_data_invalid(resource :str, errors: dict, msg: str = MSG_INVALID_DATA):
    ''' Responses 422 Unprocessable Entity '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })
    resp.status_code = 422
    return resp


def resp_exception(resource: str, description: str = '', msg: str = MSG_EXCEPTION):
    # Responses 500

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })
    resp.status_code = 500
    return resp


def resp_does_not_exist(resource :str, description :str):
    ''' Responses 404 Not Found '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': MSG_DOES_NOT_EXIST.format(description),
    })
    resp.status_code = 404
    return resp


def resp_already_exists(resource: str, description: str):
    # Responses 400

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')
    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description),
    })
    resp.status_code = 400
    return resp


def resp_ok_with_message(message: str, data=None, **extras):
    # Responses 200

    response = {'message': message}
    if data:
        response['data'] = data
    response.update(extras)
    resp = jsonify(response)
    resp.status_code = 200
    return resp


def resp_ok(data):
    resp = jsonify(data)
    resp.status_code = 200
    return resp


def resp_list_ok(data):
    resp = jsonify(data)
    resp.status_code = 200
    return resp
