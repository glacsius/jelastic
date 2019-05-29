from flask_restplus import Api
from api.respostas import RESP_500_DOC


api = Api(version='1.0', title='API Sistema AKS',
          description='API de comunicação com o Sistema AKS')


@api.errorhandler
def default_error_handler(e):
    return {'message': RESP_500_DOC, 'exception': str(e)}, 500

