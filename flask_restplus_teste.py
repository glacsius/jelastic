from flask import Flask
from flask_restplus import Api, Resource, fields


app = Flask(__name__)
api = Api(app, version='1.0', title='Minha API', description="Comedor de churros")

ns = api.namespace('todos', description='TODO operacoes')

todo = api.model('Todo', {'id': fields.Integer(description='É a id'),
                          'nome': fields.String(description='Nome do kra')})

cliente = api.model('Cliente', {'id': fields.Integer, 'nome': fields.String})
clientes = [{"id":1, "nome": 'Glaucio'}, {"id":2, "nome": 'Cristina'}]

class Todo(object):
    def get(self, id):
        return 'glaucio'


@ns.route('/')
class TodList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.marshal_list_with(todo)
    def get(self):
        return "Loko"

@ns.route('/cliente')
@ns.route('/cliente/<id>')
class Cliente(Resource):
    @ns.marshal_list_with(cliente)
    def get(self, id=None):
        if id:
            return clientes[int(id)]
        else:
            return clientes


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)