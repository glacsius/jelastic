from flask_restplus import Resource, fields
from api.apirestplus import api
from flask import request


ns = api.namespace('categories', description='Testando testas  :0)')


teste_fields = api.model('Teste', {
    'age': fields.Integer(min=10, required=True),
    'nome': fields.String(required=True, description='Nome do cara', help='Está faltando o nome',
                          default='Churros default', title="Titulo da bagaça", example='Exmeplo')
})


@ns.route('/')
class CategoryCollection(Resource):

    def get(self):
        new = api.payload
        return {'msg': 'meu teste'}

    @api.marshal_with(teste_fields, code=201, description='Object created')
    @api.expect(teste_fields)
    def post(self):
        data = api.payload
        print(data)
        return {'message': request.get_json()}
