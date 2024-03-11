from models.decision import Decision, db
from flask import make_response, jsonify
from traceback import format_exc


class DecisionService:

    @classmethod
    def create_decision(cls, decision_data):
        try:
            decision = Decision(
                decision_result=decision_data["decision_result"],
            )
            print("decision", decision)
            db.session.add(decision)
            db.session.commit()
            return decision
        except Exception as e:
            print(f"Error creating decision: {e}")
            #print(format_exc())  # Print the traceback
            return 500, "Internal server error"

    @classmethod
    def get_all_decisions(cls):
        try:
            decision = Decision.query.all()
            return decision, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting decision '}), 500)

    @classmethod
    def get_decision_by_id(cls, decision_id):
        try:
            decision = Decision.query.filter_by(decision_id).first()
            if not decision:
                return jsonify({'error': 'decision not found'})
            else:
                return decision, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting decision '}), 500)

    @classmethod
    def update_decision(cls, decision_id, decision_data):
        try:
            decision = Decision.query.filter_by(id=decision_id).first()
            if not decision:
                return jsonify({'error': 'decision not found'})

            for key,value in decision_data.items():
                setattr(decision_data,key,value)

            db.session.commit()

            updated_decision = Decision.query.get(decision_id)
            return updated_decision, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting decision '}), 500)

    @classmethod
    def delete_decision(cls, decision_id):
        try:
            decision = Decision.query.get(decision_id)
            if not decision:
                return jsonify({'error': 'decision not found'})
            else:
                db.session.delete(decision)
                db.session.commit()
                return {'message': {f'decision with Id {decision_id} deleted successfully'}},200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting decision '}), 500)
