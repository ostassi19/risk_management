from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from services.trigger_event_service import TriggerEventService

trigger_event_controller = Namespace('trigger_event', description='Trigger Event entity')

# Define the model for Trigger Event
trigger_event_model = trigger_event_controller.model('trigger_event', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "code_type": fields.String(description="code type"),
    "type": fields.String(description="type"),
    "code": fields.String(description="code"),
    "event": fields.String(description="event"),
    "standard_natural_exposure": fields.Integer(description="standard natural exposure"),
    "decision_natural_exposure": fields.Integer(description="decision natural exposure"),
    "result_natural_exposure": fields.Integer(description="result natural exposure"),
    "comment": fields.String(description="comment"),
    "selected": fields.Boolean(description="selected"),
})

@trigger_event_controller.route('/')
@trigger_event_controller.response(500, 'Internal server error')
class TriggerEventResource(Resource):
    @trigger_event_controller.marshal_with(trigger_event_model, description="Trigger Event created successfully")
    @trigger_event_controller.expect(trigger_event_model)
    @trigger_event_controller.response(201, "{'message': 'Trigger Event registered}")
    def post(self):
        """
        Create a new Trigger Event.
        """
        trigger_event_data = request.json
        return TriggerEventService.create_trigger_event(trigger_event_data), 201

    @trigger_event_controller.marshal_list_with(trigger_event_model, code=200, description="Success")
    @trigger_event_controller.response(200, "{'message': 'success}")
    @trigger_event_controller.response(404, "{'message': 'not found}")
    def get(self):
        """
        Get all Trigger Events.
        """
        return TriggerEventService.get_all_trigger_events()

@trigger_event_controller.route('/<int:trigger_event_id>')
@trigger_event_controller.param('trigger_event_id', 'the Trigger Event identifier')
@trigger_event_controller.response(500, 'Internal server error')
class TriggerEventDetailResource(Resource):
    @trigger_event_controller.marshal_with(trigger_event_model, description="get Trigger Event by id")
    @trigger_event_controller.response(200, 'success')
    @trigger_event_controller.response(404, "Trigger Event not found")
    def get(self, trigger_event_id):
        """
        Get details of a specific Trigger Event.
        """
        trigger_event = TriggerEventService.get_trigger_event_by_id(trigger_event_id)
        if trigger_event:
            return trigger_event
        return {"message": "Trigger Event not found"}, 404

    @trigger_event_controller.marshal_with(trigger_event_model, description="update Trigger Event")
    @trigger_event_controller.response(404, "Trigger Event not found")
    @trigger_event_controller.response(200, 'success')
    @trigger_event_controller.expect(trigger_event_model)
    def put(self, trigger_event_id):
        """
        Update details of a specific Trigger Event.
        """
        trigger_event_data = request.json
        updated_trigger_event = TriggerEventService.update_trigger_event(trigger_event_id, trigger_event_data)
        if updated_trigger_event:
            return updated_trigger_event
        return {"message": "Trigger Event not found"}, 404

    @trigger_event_controller.marshal_with(trigger_event_model, code=200, description="Success")
    @trigger_event_controller.response(404, "Trigger Event not found")
    def delete(self, trigger_event_id):
        """
        Delete a specific Trigger Event.
        """
        deleted_trigger_event = TriggerEventService.delete_trigger_event(trigger_event_id)
        if deleted_trigger_event:
            return deleted_trigger_event
        return {"message": "Trigger Event not found"}, 404
