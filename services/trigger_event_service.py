from models.trigger_event import TriggerEvent, db
from flask import make_response, jsonify

class TriggerEventService:

    @classmethod
    def create_trigger_event(cls, trigger_event_data):
        try:
            if trigger_event_data["decision_natural_exposure"]:
                result_natural_exposure = trigger_event_data["decision_natural_exposure"]
            else:
                result_natural_exposure = trigger_event_data["standard_natural_exposure"]

            print("result_natural_exposure ",result_natural_exposure)
            trigger_event = TriggerEvent(
                code_type=trigger_event_data["code_type"],
                type=trigger_event_data["type"],
                code=trigger_event_data["code"],
                event=trigger_event_data["event"],
                standard_natural_exposure=trigger_event_data["standard_natural_exposure"],
                decision_natural_exposure=trigger_event_data["decision_natural_exposure"],
                result_natural_exposure=result_natural_exposure,
                comment=trigger_event_data["comment"],
            )
            db.session.add(trigger_event)
            db.session.commit()
            return 200, trigger_event
        except Exception as e:
            return make_response(jsonify({'message': 'Error creating Trigger Event'}), 500)

    @classmethod
    def get_all_trigger_events(cls):
        try:
            trigger_events = TriggerEvent.query.all()
            return trigger_events, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Trigger Events'}), 500)

    @classmethod
    def get_trigger_event_by_id(cls, trigger_event_id):
        try:
            trigger_event = TriggerEvent.query.filter_by(id=trigger_event_id).first()
            if not trigger_event:
                return jsonify({'error': 'Trigger Event not found'})
            else:
                return trigger_event, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Trigger Event'}), 500)

    @classmethod
    def update_trigger_event(cls, trigger_event_id, trigger_event_data):
        try:
            trigger_event = TriggerEvent.query.filter_by(id=trigger_event_id).first()
            print("ps",trigger_event)
            if trigger_event_data["decision_natural_exposure"]:
                result_natural_exposure = trigger_event_data["decision_natural_exposure"]
            else:
                result_natural_exposure = trigger_event_data["standard_natural_exposure"]
            if not trigger_event:
                return jsonify({'error': 'Trigger Event not found'})

            for key, value in trigger_event_data.items():
                setattr(trigger_event, key, value)

            # Set the result_natural_exposure in the trigger_event
            setattr(trigger_event, "result_natural_exposure", result_natural_exposure)
            db.session.commit()

            updated_trigger_event = TriggerEvent.query.get(trigger_event_id)
            return updated_trigger_event, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error updating Trigger Event'}), 500)

    @classmethod
    def delete_trigger_event(cls, trigger_event_id):
        try:
            trigger_event = TriggerEvent.query.get(trigger_event_id)
            if not trigger_event:
                return jsonify({'error': 'Trigger Event not found'})
            else:
                db.session.delete(trigger_event)
                db.session.commit()
                return {'message': f'Trigger Event with Id {trigger_event_id} deleted successfully'}, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error deleting Trigger Event'}), 500)

