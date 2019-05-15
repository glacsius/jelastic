from flask_restplus import Namespace, Resource

ns_pastas = Namespace('pastas', description='Cadastro de pastas')

@ns_pastas.route('/')
class Pastas(Resource):
    def get(self):
        return 'Pastassssss'