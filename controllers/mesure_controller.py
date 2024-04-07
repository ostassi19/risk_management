from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify

from services.mesure_service import MeasureService

measure_controller = Namespace('measure', description='Measure entity')

# Adjust the model fields based on the updated measure entity
measure_model = measure_controller.model('measure', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "measure": fields.String(required=True, description="measure"),
    "type": fields.String(required=True, description="measure type"),
    "measure_level_id": fields.Integer(description="measure_level id"),
})


@measure_controller.route('/')
@measure_controller.response(500, 'Internal server error')
class MeasureResource(Resource):
    @measure_controller.marshal_with(measure_model, description="measure created successfully")
    @measure_controller.expect(measure_model)
    @measure_controller.response(201, "{'message': 'measure registered ")
    # @jwt_required()
    def post(self):
        """
        Create a new measure.
        """
        measure_data = request.json
        return MeasureService.create_measure(measure_data), 201

    @measure_controller.marshal_list_with(measure_model, code=200, description="Success")
    @measure_controller.response(200, "{'message': 'success ")
    @measure_controller.response(404, "{'message': 'not found ")
    # @jwt_required()
    def get(self):
        """
        Get all measures.
        """
        return MeasureService.get_all_measures()


@measure_controller.route('/<int:measure_id>')
@measure_controller.param('measure_id', 'the measure identifier')
@measure_controller.response(500, 'Internal server error')
class MeasureDetailResource(Resource):
    @measure_controller.marshal_with(measure_model, description="get measure by id")
    @measure_controller.response(200, 'success')
    @measure_controller.response(404, "Measure not found")
    # @jwt_required()
    def get(self, measure_id):
        """
        Get details of a specific measure.
        """
        measure = MeasureService.get_measure_by_id(measure_id)
        if measure:
            return measure
        return {"message": "measure not found"}, 404

    @measure_controller.marshal_with(measure_model, description="update measure")
    @measure_controller.response(404, "Measure not found")
    @measure_controller.response(200, 'success')
    @measure_controller.expect(measure_model)
    # @jwt_required()
    def put(self, measure_id):
        """
        Update details of a specific measure.
        """
        measure_data = request.json
        updated_measure = MeasureService.update_measure(measure_id, measure_data)
        if updated_measure:
            return updated_measure
        return {"message": "Measure not found"}, 404

    @measure_controller.marshal_with(measure_model, code=200, description="Success")
    @measure_controller.response(404, "measure not found")
    # @jwt_required()
    def delete(self, measure_id):
        """
        Delete a specific measure.
        """
        deleted_measure = MeasureService.delete_measure(measure_id)
        if deleted_measure:
            return deleted_measure
        return {"message": "Measure not found"}, 404
