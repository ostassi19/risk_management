from flask_restx import Api
from controllers.damage_controller import damage_controller
from controllers.trigger_controller import trigger_event_controller
from controllers.risk_controller import risk_controller
from controllers.mesure_controller import mesure_controller
from controllers.support_actif_controller import support_actif_controller
from controllers.pimary_actif_controller import primary_actif_controller
from controllers.authentication_controller import auth_controller
from flask import Blueprint


api_v1 = Blueprint('api', __name__, url_prefix='/')
authorizations = {"Bearer": {"type": "apiKey",
                             "in": "header", "name": "Authorization"}}

api = Api(api_v1,
          title='RISKMANAGEMENT RESTFULL API',
          version='1.0',
          description='an API for riskManagement project',
          authorizations=authorizations,
          security='Bearer'
          )

api.add_namespace(risk_controller)
api.add_namespace(damage_controller)
api.add_namespace(trigger_event_controller)
api.add_namespace(mesure_controller)
api.add_namespace(support_actif_controller)
api.add_namespace(primary_actif_controller)
api.add_namespace(auth_controller)


