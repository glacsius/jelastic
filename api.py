from flask import Blueprint
from flask_restplus import Api
blueprint = Blueprint('api', __name__, url_prefix='/myapi')
api = Api(blueprint,
    title='API',
    description='API'
)

from status import api as ns1
api.add_namespace(ns1)