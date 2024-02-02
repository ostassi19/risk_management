from flask_restx import Api
from controllers.test_controller import test_controller
from flask import Blueprint


api_v1 = Blueprint('api', __name__, url_prefix='/')

api = Api(api_v1,
          title='RISKMANAGEMENT RESTFULL API',
          version='1.0',
          description='an API for riskManagement project',
          #   authorizations=authorizations,
          #   security='Bearer'
          )

api.add_namespace(test_controller)
