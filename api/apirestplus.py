from flask_restplus import Api


api = Api(version='1.0', title='API Sistema AKS',
          description='API de comunicação com o Sistema AKS')


@api.errorhandler
def default_error_handler(e):
    message = 'Erro no processamento no servidor'
    return {'message': message, 'exception': str(e)}, 500

