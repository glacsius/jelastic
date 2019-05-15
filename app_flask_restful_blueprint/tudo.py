from flask import Blueprint
from flask_restplus import Api
from app_flask_restful_blueprint.apis.api1 import ns_usuarios as ns1
from app_flask_restful_blueprint.apis.api2 import ns_pastas as ns2


blueprint = Blueprint('api',
                      __name__,
                      url_prefix=''  # ''/myapi'
                      )


api = Api(blueprint, title='API',
          description='API'
          )


api.add_namespace(ns1)
api.add_namespace(ns2)
