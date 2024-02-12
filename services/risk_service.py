from models.risk import Risk, db
from flask import make_response, jsonify

class RiskService:

    @classmethod
    def create_risk(cls, risk_data):
        try:
            risk = Risk(
                consequence_type=risk_data["consequence_type"],
                intrinsic_impact=risk_data["intrinsic_impact"],
                personalized_intrinsic_impact=risk_data["personalized_intrinsic_impact"],
                intrinsic_gravity=risk_data["intrinsic_gravity"],
                intrinsic_potential=risk_data["intrinsic_potential"],
                residual_potential=risk_data["residual_potential"],
                personalized_residual_potential=risk_data["personalized_residual_potential"],
                residual_impact=risk_data["residual_impact"],
                decision=risk_data["decision"],
                residual_gravity=risk_data["residual_gravity"],
                damage_id=risk_data["damage_id"],
                mesure_id=risk_data["mesure_id"],
                support_actif_id=risk_data["support_actif_id"],
                trigger_event_id=risk_data["trigger_event_id"],


            )
            db.session.add(risk)
            db.session.commit()
            return 200, risk
        except Exception as e:
            return make_response(jsonify({'message': 'Error creating Risk'}), 500)

    @classmethod
    def get_all_risks(cls):
        try:
            risks = Risk.query.all()
            return risks, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Risks'}), 500)

    @classmethod
    def get_risk_by_id(cls, risk_id):
        try:
            risk = Risk.query.filter_by(id=risk_id).first()
            if not risk:
                return jsonify({'error': 'Risk not found'})
            else:
                return risk, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Risk'}), 500)

    @classmethod
    def update_risk(cls, risk_id, risk_data):
        try:
            risk = Risk.query.filter_by(id=risk_id).first()
            if not risk:
                return jsonify({'error': 'Risk not found'})

            for key, value in risk_data.items():
                setattr(risk, key, value)
            db.session.commit()

            updated_risk = Risk.query.get(risk_id)
            return updated_risk, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error updating Risk'}), 500)

    @classmethod
    def delete_risk(cls, risk_id):
        try:
            risk = Risk.query.get(risk_id)
            if not risk:
                return jsonify({'error': 'Risk not found'})
            else:
                db.session.delete(risk)
                db.session.commit()
                return {'message': f'Risk with Id {risk_id} deleted successfully'}, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error deleting Risk'}), 500)
