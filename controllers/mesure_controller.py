from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify

from controllers.mesure_level_controller import mesure_level_model
from services.mesure_service import MesureService

mesure_controller = Namespace('mesure', description='Mesure entity')

# Adjust the model fields based on the updated Mesure entity
mesure_model = mesure_controller.model('mesure', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "measure": fields.String(required=True, description="measure"),
    "type": fields.String(required=True, description="mesure type"),
    #"level": fields.Nested(mesure_level_model,required=False)
    # Add fields specific to each mesure type as needed
})

@mesure_controller.route('/')
@mesure_controller.response(500, 'Internal server error')
class MesureResource(Resource):
    @mesure_controller.marshal_with(mesure_model, description="Mesure created successfully")
    @mesure_controller.expect(mesure_model)
    @mesure_controller.response(201, "{'message': 'mesure registered ")
    @jwt_required()
    def post(self):
        """
        Create a new mesure.
        """
        mesure_data = request.json
        return MesureService.create_mesure(mesure_data), 201

    @mesure_controller.marshal_list_with(mesure_model, code=200, description="Success")
    @mesure_controller.response(200, "{'message': 'success ")
    @mesure_controller.response(404, "{'message': 'not found ")
    @jwt_required()
    def get(self):
        """
        Get all mesures.
        """
        return MesureService.get_all_mesures()

@mesure_controller.route('/<int:mesure_id>')
@mesure_controller.param('mesure_id', 'the mesure identifier')
@mesure_controller.response(500, 'Internal server error')
class MesureDetailResource(Resource):
    @mesure_controller.marshal_with(mesure_model, description="get mesure by id")
    @mesure_controller.response(200, 'success')
    @mesure_controller.response(404, "Mesure not found")
    @jwt_required()
    def get(self, mesure_id):
        """
        Get details of a specific mesure.
        """
        mesure = MesureService.get_mesure_by_id(mesure_id)
        if mesure:
            return mesure
        return {"message": "Mesure not found"}, 404

    @mesure_controller.marshal_with(mesure_model, description="update mesure")
    @mesure_controller.response(404, "Mesure not found")
    @mesure_controller.response(200, 'success')
    @mesure_controller.expect(mesure_model)
    @jwt_required()
    def put(self, mesure_id):
        """
        Update details of a specific mesure.
        """
        mesure_data = request.json
        updated_mesure = MesureService.update_mesure(mesure_id, mesure_data)
        if updated_mesure:
            return updated_mesure
        return {"message": "Mesure not found"}, 404

    @mesure_controller.marshal_with(mesure_model, code=200, description="Success")
    @mesure_controller.response(404, "Mesure not found")
    @jwt_required()
    def delete(self, mesure_id):
        """
        Delete a specific mesure.
        """
        deleted_mesure = MesureService.delete_mesure(mesure_id)
        if deleted_mesure:
            return deleted_mesure
        return {"message": "Mesure not found"}, 404
