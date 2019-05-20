from flask_restplus import Resource
from api.apirestplus import api


ns = api.namespace('categories', description='Operations related to blog categories')


@ns.route('/')
class CategoryCollection(Resource):

    def get(self):
        return {'msg': 'meu teste'}
