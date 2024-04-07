from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request
from services.mesure_level_service import MesureLevelService

mesure_level_controller = Namespace('mesure_level', description='MesureLevel entity')

mesure_level_model = mesure_level_controller.model('mesure_level', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "level": fields.String(required=True, description="level"),
    "description": fields.String(required=True, description="description"),
    "definition": fields.String(required=True, description="definition"),
})

@mesure_level_controller.route('/')
@mesure_level_controller.response(500, 'Internal server error')
class DecisionResource(Resource):
    @mesure_level_controller.marshal_with(mesure_level_model, description="MesureLevel created successfully")
    @mesure_level_controller.expect(mesure_level_model)
    @mesure_level_controller.response(201, "{'message': 'mesureLevel registered ")
    #@jwt_required()
    def post(self):
        """
        Create a new mesureLevel.
        """
        mesure_level_data = request.json
        return MesureLevelService.create_mesure_level(mesure_level_data)

    @mesure_level_controller.marshal_list_with(mesure_level_model, code=200, description="Success")
    @mesure_level_controller.response(200, "{'message': 'success ")
    @mesure_level_controller.response(404, "{'message': 'not found ")
    #@jwt_required()
    def get(self):
        """
        Get all decisions.
        """
        return MesureLevelService.get_all_mesure_levels()

@mesure_level_controller.route('/<int:decision_id>')
@mesure_level_controller.param('decision_id', 'the mesure level identifier')
@mesure_level_controller.response(500, 'Internal server error')
class MesureLevelDetailResource(Resource):
    @mesure_level_controller.marshal_with(mesure_level_model, description="get mesure level by id")
    @mesure_level_controller.response(200, 'success')
    @mesure_level_controller.response(404, "Mesure level not found")
    #@jwt_required()
    def get(self, mesure_level_id):
        """
        Get details of a specific mesure_level.
        """
        mesure_level = MesureLevelService.get_mesure_level_by_id(mesure_level_id)
        if mesure_level:
            return mesure_level
        return {"message": "MesureLevel not found"}, 404

    @mesure_level_controller.marshal_with(mesure_level_model, description="update mesure level")
    @mesure_level_controller.response(404, "Mesure level not found")
    @mesure_level_controller.response(200, 'success')
    @mesure_level_controller.expect(mesure_level_model)
    #@jwt_required()
    def put(self, mesure_level_id):
        """
        Update details of a specific mesure_level.
        """
        mesure_level_data = request.json
        updated_mesure_level = MesureLevelService.update_mesure_level(mesure_level_id, mesure_level_data)
        if updated_mesure_level:
            return updated_mesure_level
        return {"message": "MesureLevel not found"}, 404

    @mesure_level_controller.marshal_with(mesure_level_model, code=200, description="Success")
    @mesure_level_controller.response(404, "mesure level not found")
    #@jwt_required()
    def delete(self, mesure_level_id):
        """
        Delete a specific decision.
        """
        deleted_mesure_level = MesureLevelService.delete_mesure_level(mesure_level_id)
        if deleted_mesure_level:
            return deleted_mesure_level
        return {"message": "MesureLevel not found"}, 404
