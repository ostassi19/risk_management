from models.mesure_level import MeasureLevel, db
from flask import make_response, jsonify
from traceback import format_exc


class MesureLevelService:

    @classmethod
    def create_mesure_level(cls, mesure_level_data):
        try:
            mesure_level = MeasureLevel(
                level=mesure_level_data["level"],
                description=mesure_level_data["description"],
                definition=mesure_level_data["definition"],
            )
            db.session.add(mesure_level)
            db.session.commit()
            return mesure_level
        except Exception as e:
            print(f"Error creating mesure_level: {e}")
            #print(format_exc())  # Print the traceback
            return 500, "Internal server error"

    @classmethod
    def get_all_mesure_levels(cls):
        try:
            mesure_level = MeasureLevel.query.all()
            return mesure_level, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting mesure_level '}), 500)

    @classmethod
    def get_mesure_level_by_id(cls, mesure_level_id):
        try:
            mesure_level = MeasureLevel.query.filter_by(mesure_level_id).first()
            if not mesure_level:
                return jsonify({'error': 'mesure_level not found'})
            else:
                return mesure_level, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting mesure_level '}), 500)

    @classmethod
    def update_mesure_level(cls, mesure_level_id, mesure_level_data):
        try:
            mesure_level = MeasureLevel.query.filter_by(id=mesure_level_id).first()
            if not mesure_level:
                return jsonify({'error': 'mesure_level not found'})

            for key,value in mesure_level_data.items():
                setattr(mesure_level_data,key,value)

            db.session.commit()

            updated_mesure_level = MeasureLevel.query.get(mesure_level_id)
            return updated_mesure_level, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting mesure_level '}), 500)

    @classmethod
    def delete_mesure_level(cls, mesure_level_id):
        try:
            mesure_level = MeasureLevel.query.get(mesure_level_id)
            if not mesure_level:
                return jsonify({'error': 'mesure_level not found'})
            else:
                db.session.delete(mesure_level)
                db.session.commit()
                return {'message': {f'mesure_level with Id {mesure_level_id} deleted successfully'}},200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting mesure_level '}), 500)
