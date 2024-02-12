from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from services.support_actif_service import SupportActifService

support_actif_controller = Namespace('support_actif', description='Support Actif entity')

# Define the model for Support Actif
support_actif_model = support_actif_controller.model('alaamani', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "name": fields.String(description="name"),
    "type": fields.String(description="type"),
    "element": fields.String(description="element"),
    "selection": fields.Boolean(description="selection"),
})


@support_actif_controller.route('/')
@support_actif_controller.response(500, 'Internal server error')
class AlaAmaniResource(Resource):
    @support_actif_controller.marshal_with(support_actif_model, description="Support Actif created successfully")
    @support_actif_controller.expect(support_actif_model)
    @support_actif_controller.response(201, "{'message': 'Support Actif registered}")
    def post(self):
        """
        Create a new Support Actif.
        """
        support_actif_data = request.json
        return SupportActifService.create_support_actif(support_actif_data), 201

    @support_actif_controller.marshal_list_with(support_actif_model, code=200, description="Success")
    @support_actif_controller.response(200, "{'message': 'success}")
    @support_actif_controller.response(404, "{'message': 'not found}")
    def get(self):
        """
        Get all Support Actifs.
        """
        return SupportActifService.get_all_support_actifs()


@support_actif_controller.route('/<int:support_actif_id>')
@support_actif_controller.param('support_actif_id', 'the Support Actif identifier')
@support_actif_controller.response(500, 'Internal server error')
class AlaAmaniDetailResource(Resource):
    @support_actif_controller.marshal_with(support_actif_model, description="get Support Actif by id")
    @support_actif_controller.response(200, 'success')
    @support_actif_controller.response(404, "Support Actif not found")
    def get(self, support_actif_id):
        """
        Get details of a specific Support Actif.
        """
        support_actif = SupportActifService.get_support_actif_by_id(support_actif_id)
        if support_actif:
            return support_actif
        return {"message": "Support Actif not found"}, 404

    @support_actif_controller.marshal_with(support_actif_model, description="update Support Actif")
    @support_actif_controller.response(404, "Support Actif not found")
    @support_actif_controller.response(200, 'success')
    @support_actif_controller.expect(support_actif_model)
    def put(self, support_actif_id):
        """
        Update details of a specific Support Actif.
        """
        support_actif_data = request.json
        updated_support_actif = SupportActifService.update_support_actif(support_actif_id, support_actif_data)
        if updated_support_actif:
            return updated_support_actif
        return {"message": "Support Actif not found"}, 404

    @support_actif_controller.marshal_with(support_actif_model, code=200, description="Success")
    @support_actif_controller.response(404, "Support Actif not found")
    def delete(self, support_actif_id):
        """
        Delete a specific Support Actif.
        """
        deleted_support_actif = SupportActifService.delete_support_actif(support_actif_id)
        if deleted_support_actif:
            return deleted_support_actif
        return {"message": "Support Actif not found"}, 404
