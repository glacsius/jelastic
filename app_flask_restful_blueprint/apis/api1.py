from flask_restplus import Namespace, Resource


ns_usuarios = Namespace('usuarios', description='Cadastro de usuario')


@ns_usuarios.route('/')
class Usuarios(Resource):
    def get(self):
        return 'Hellllllllllloooo'
