from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify

from services.risk_service import RiskService

risk_controller = Namespace('risk', description='Risk entity')

# Define the model for Risk
risk_model = risk_controller.model('risk', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "consequence_type": fields.String(description="consequence type"),
    "intrinsic_impact": fields.Integer(description="intrinsic impact"),
    "personalized_intrinsic_impact": fields.Integer(description="personalized intrinsic impact"),
    "intrinsic_gravity": fields.Integer(description="intrinsic gravity"),
    "intrinsic_potential": fields.Integer(description="intrinsic potential"),
    "residual_potential": fields.Integer(description="residual potential"),
    "personalized_residual_potential": fields.Integer(description="personalized residual potential"),
    "residual_impact": fields.Integer(description="residual impact"),
    "comment": fields.String(description="comment"),
    "residual_gravity": fields.Integer(description="residual gravity"),
    "mesure_id": fields.Integer(default=None,description="mesure id" ),
    "support_actif_id": fields.Integer(description="support_actif id"),
    "damage_id": fields.Integer(description="damage id"),
    "primary_actif_id": fields.Integer(description="primary_actif id"),
    "trigger_event_id": fields.Integer(description="trigger_event id"),
    "decision_id": fields.Integer(description="decision id"),

})


@risk_controller.route('/')
@risk_controller.response(500, 'Internal server error')
class RiskResource(Resource):
    @risk_controller.marshal_with(risk_model, description="Risk created successfully")
    @risk_controller.expect(risk_model)
    @risk_controller.response(201, "{'message': 'Risk registered}")
    #@jwt_required()
    def post(self):
        """
        Create a new Risk.
        """
        risk_data = request.json
        return RiskService.create_new_risk(risk_data), 201

    @risk_controller.marshal_list_with(risk_model, code=200, description="Success")
    @risk_controller.response(200, "{'message': 'success}")
    @risk_controller.response(404, "{'message': 'not found}")
    @jwt_required()
    def get(self):
        """
        Get all Risks.
        """
        return RiskService.get_all_risks()


@risk_controller.route('/<int:risk_id>')
@risk_controller.param('risk_id', 'the Risk identifier')
@risk_controller.response(500, 'Internal server error')
class RiskDetailResource(Resource):
    @risk_controller.marshal_with(risk_model, description="get Risk by id")
    @risk_controller.response(200, 'success')
    @risk_controller.response(404, "Risk not found")
    @jwt_required()
    def get(self, risk_id):
        """
        Get details of a specific Risk.
        """
        risk = RiskService.get_risk_by_id(risk_id)
        if risk:
            return risk
        return {"message": "Risk not found"}, 404

    @risk_controller.marshal_with(risk_model, description="update Risk")
    @risk_controller.response(404, "Risk not found")
    @risk_controller.response(200, 'success')
    @risk_controller.expect(risk_model)
    #@jwt_required()
    def put(self, risk_id):
        """
        Update details of a specific Risk.
        """
        risk_data = request.json
        updated_risk = RiskService.update_risk(risk_id, risk_data)
        if updated_risk:
            return updated_risk
        return {"message": "Risk not found"}, 404

    @risk_controller.marshal_with(risk_model, code=200, description="Success")
    @risk_controller.response(404, "Risk not found")
    @jwt_required()
    def delete(self, risk_id):
        """
        Delete a specific Risk.
        """
        deleted_risk = RiskService.delete_risk(risk_id)
        if deleted_risk:
            return deleted_risk
        return {"message": "Risk not found"}, 404
