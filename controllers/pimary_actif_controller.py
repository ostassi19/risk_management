from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from services.primary_actif_service import PrimaryActifService

primary_actif_controller = Namespace('primary_actif', description='Primary Actif entity')

# Define the model for Primary Actif
primary_actif_model = primary_actif_controller.model('primary_actif', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "code": fields.String(description="code"),
    "description": fields.String(description="description"),
    "complementary_description": fields.String(description="complementary description"),
    "actif_type": fields.String(description="actif type"),
    "impact_level": fields.String(description="impact level"),
})

@primary_actif_controller.route('/')
@primary_actif_controller.response(500, 'Internal server error')
class PrimaryActifResource(Resource):
    @primary_actif_controller.marshal_with(primary_actif_model, description="Primary Actif created successfully")
    @primary_actif_controller.expect(primary_actif_model)
    @primary_actif_controller.response(201, "{'message': 'Primary Actif registered}")
    @jwt_required()
    def post(self):
        """
        Create a new Primary Actif.
        """
        primary_actif_data = request.json
        return PrimaryActifService.create_primary_actif(primary_actif_data), 201

    @primary_actif_controller.marshal_list_with(primary_actif_model, code=200, description="Success")
    @primary_actif_controller.response(200, "{'message': 'success}")
    @primary_actif_controller.response(404, "{'message': 'not found}")
    @jwt_required()
    def get(self):
        """
        Get all Primary Actifs.
        """
        return PrimaryActifService.get_all_primary_actifs()

@primary_actif_controller.route('/<int:primary_actif_id>')
@primary_actif_controller.param('primary_actif_id', 'the Primary Actif identifier')
@primary_actif_controller.response(500, 'Internal server error')
class PrimaryActifDetailResource(Resource):
    @primary_actif_controller.marshal_with(primary_actif_model, description="get Primary Actif by id")
    @primary_actif_controller.response(200, 'success')
    @primary_actif_controller.response(404, "Primary Actif not found")
    @jwt_required()
    def get(self, primary_actif_id):
        """
        Get details of a specific Primary Actif.
        """
        primary_actif = PrimaryActifService.get_primary_actif_by_id(primary_actif_id)
        if primary_actif:
            return primary_actif
        return {"message": "Primary Actif not found"}, 404

    @primary_actif_controller.marshal_with(primary_actif_model, description="update Primary Actif")
    @primary_actif_controller.response(404, "Primary Actif not found")
    @primary_actif_controller.response(200, 'success')
    @primary_actif_controller.expect(primary_actif_model)
    @jwt_required()
    def put(self, primary_actif_id):
        """
        Update details of a specific Primary Actif.
        """
        primary_actif_data = request.json
        updated_primary_actif = PrimaryActifService.update_primary_actif(primary_actif_id, primary_actif_data)
        if updated_primary_actif:
            return updated_primary_actif
        return {"message": "Primary Actif not found"}, 404

    @primary_actif_controller.marshal_with(primary_actif_model, code=200, description="Success")
    @primary_actif_controller.response(404, "Primary Actif not found")
    @jwt_required()
    def delete(self, primary_actif_id):
        """
        Delete a specific Primary Actif.
        """
        deleted_primary_actif = PrimaryActifService.delete_primary_actif(primary_actif_id)
        if deleted_primary_actif:
            return deleted_primary_actif
        return {"message": "Primary Actif not found"}, 404
