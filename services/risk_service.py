import traceback

from models.risk import Risk, db
from flask import make_response, jsonify

from services.damage_service import DamageService
from services.mesure_service import MeasureService
from services.support_actif_service import SupportActifService
from services.trigger_event_service import TriggerEventService
from utils.calcul import calcul_gravity


class RiskService:


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
            gravity_intrinsic = calcul_gravity(risk_data["intrinsic_impact"], risk_data["intrinsic_potential"]) if \
                risk_data["intrinsic_impact"] and risk_data["intrinsic_potential"] else 0
            gravity_residual = calcul_gravity(risk_data["residual_impact"], risk_data["residual_potential"]) if \
                risk_data["intrinsic_impact"] and risk_data["intrinsic_potential"] else 0
            if not risk:
                return jsonify({'error': 'Risk not found'})

            measure = MeasureService.create_measure(risk_data["measure"])

            for key, value in risk_data.items():
                setattr(risk, key, value)
            setattr(risk, "intrinsic_gravity", gravity_intrinsic)
            setattr(risk, "residual_gravity", gravity_residual)
            setattr(risk, "measure_id", measure[1])
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

    @classmethod
    def create(cls, risk_data):
        try:
            gravity_intrinsic = calcul_gravity(risk_data["intrinsic_impact"], risk_data["intrinsic_potential"]) if \
                risk_data["intrinsic_impact"] and risk_data["intrinsic_potential"] else 0
            gravity_residual = calcul_gravity(risk_data["residual_impact"], risk_data["residual_potential"]) if \
                risk_data["intrinsic_impact"] and risk_data["intrinsic_potential"] else 0
            measure = MeasureService.create_measure(risk_data["measure"])
            risk = Risk(
                consequence_type=risk_data["consequence_type"],
                intrinsic_impact=risk_data["intrinsic_impact"],
                personalized_intrinsic_impact=risk_data["personalized_intrinsic_impact"],
                intrinsic_gravity=gravity_intrinsic,
                intrinsic_potential=risk_data["intrinsic_potential"],
                residual_potential=risk_data["residual_potential"],
                personalized_residual_potential=risk_data["personalized_residual_potential"],
                residual_impact=risk_data["residual_impact"],
                comment=risk_data["comment"],
                residual_gravity=gravity_residual,
                measure_id=measure[1],
                support_actif_id=risk_data["support_actif_id"],
                damage_id=risk_data["damage_id"],
                primary_actif_id=risk_data["primary_actif_id"],
                trigger_event_id=risk_data["trigger_event_id"],
                decision_id=risk_data["decision_id"],
            )
            db.session.add(risk)
            db.session.commit()

            if risk_data["trigger_event_id"]:
                trigger_event = TriggerEventService.get_trigger_event_by_id(risk_data["trigger_event_id"])
                setattr(trigger_event[0], "selection", True)
                db.session.commit()
            if risk_data["support_actif_id"]:
                support_actif = SupportActifService.get_support_actif_by_id(risk_data["support_actif_id"])
                setattr(support_actif[0], "selection", True)
                db.session.commit()

            if risk_data["damage_id"]:
                damage = DamageService.get_damage_by_id(risk_data["damage_id"])
                setattr(damage[0], "selection", True)
                db.session.commit()

            return risk, 201
        except Exception as e:
            traceback.print_exc()  # Print the traceback
            return make_response(jsonify({'message': 'Error creating Risk'}), 500)
