from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request
from services.decision_service import DecisionService

decision_controller = Namespace('decision', description='Decision entity')

decision_model = decision_controller.model('decision', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "decision_result": fields.String(required=True, description="security impact"),
})

@decision_controller.route('/')
@decision_controller.response(500, 'Internal server error')
class DecisionResource(Resource):
    @decision_controller.marshal_with(decision_model, description="Decision created successfully")
    @decision_controller.expect(decision_model)
    @decision_controller.response(201, "{'message': 'decision registered ")
    @jwt_required()
    def post(self):
        """
        Create a new decision.
        """
        decision_data = request.json
        return DecisionService.create_decision(decision_data)

    @decision_controller.marshal_list_with(decision_model, code=200, description="Success")
    @decision_controller.response(200, "{'message': 'success ")
    @decision_controller.response(404, "{'message': 'not found ")
    #@jwt_required()
    def get(self):
        """
        Get all decisions.
        """
        return DecisionService.get_all_decisions()

@decision_controller.route('/<int:decision_id>')
@decision_controller.param('decision_id', 'the decision identifier')
@decision_controller.response(500, 'Internal server error')
class DecisionDetailResource(Resource):
    @decision_controller.marshal_with(decision_model, description="get decision by id")
    @decision_controller.response(200, 'success')
    @decision_controller.response(404, "Decision not found")
    #@jwt_required()
    def get(self, decision_id):
        """
        Get details of a specific decision.
        """
        decision = DecisionService.get_decision_by_id(decision_id)
        if decision:
            return decision
        return {"message": "Decision not found"}, 404

    @decision_controller.marshal_with(decision_model, description="update decision")
    @decision_controller.response(404, "Decision not found")
    @decision_controller.response(200, 'success')
    @decision_controller.expect(decision_model)
    @jwt_required()
    def put(self, decision_id):
        """
        Update details of a specific decision.
        """
        decision_data = request.json
        updated_decision = DecisionService.update_decision(decision_id, decision_data)
        if updated_decision:
            return updated_decision
        return {"message": "Decision not found"}, 404

    @decision_controller.marshal_with(decision_model, code=200, description="Success")
    @decision_controller.response(404, "Decision not found")
    @jwt_required()
    def delete(self, decision_id):
        """
        Delete a specific decision.
        """
        deleted_decision = DecisionService.delete_decision(decision_id)
        if deleted_decision:
            return deleted_decision
        return {"message": "Decision not found"}, 404
