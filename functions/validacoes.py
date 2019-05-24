from api.responses import resp_invalido_400


def validar_json(request, schema):
    if not request.is_json:
        return resp_invalido_400('Não contém JSON válido')

    try:
        j = request.get_json()
    except Exception as e:
        return resp_invalido_400('Aquivo JSON em formato inválido: ' + str(e))

    resp = schema.validate(j)
    if resp:
        for erro in resp:
            return resp_invalido_400(resp[erro][0])

    return None
