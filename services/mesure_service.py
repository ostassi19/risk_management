from models.mesure import Mesure, db
from flask import make_response, jsonify

class MesureService:

    @classmethod
    def create_mesure(cls, mesure_data):
        try:
            mesure = Mesure(
                level=mesure_data["level"],
                measure=mesure_data["measure"],
            )
            db.session.add(mesure)
            db.session.commit()
            return 200, mesure
        except Exception as e:
            return make_response(jsonify({'message': 'Error creating mesure'}), 500)

    @classmethod
    def get_all_mesures(cls):
        try:
            mesures = Mesure.query.all()
            return mesures, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting mesures'}), 500)

    @classmethod
    def get_mesure_by_id(cls, mesure_id):
        try:
            mesure = Mesure.query.filter_by(id=mesure_id).first()
            if not mesure:
                return jsonify({'error': 'Mesure not found'})
            else:
                return mesure, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting mesure'}), 500)

    @classmethod
    def update_mesure(cls, mesure_id, mesure_data):
        try:
            mesure = Mesure.query.filter_by(id=mesure_id).first()
            if not mesure:
                return jsonify({'error': 'Mesure not found'})

            for key, value in mesure_data.items():
                setattr(mesure, key, value)
            db.session.commit()

            updated_mesure = Mesure.query.get(mesure_id)
            return updated_mesure, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error updating mesure'}), 500)

    @classmethod
    def delete_mesure(cls, mesure_id):
        try:
            mesure = Mesure.query.get(mesure_id)
            if not mesure:
                return jsonify({'error': 'Mesure not found'})
            else:
                db.session.delete(mesure)
                db.session.commit()
                return {'message': f'Mesure with Id {mesure_id} deleted successfully'}, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error deleting mesure'}), 500)
