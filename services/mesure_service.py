from models.measure import Measure, db
from flask import make_response, jsonify


class MeasureService:

    @classmethod
    def create_measure(cls, measure_data):
        try:
            measure = Measure(
                measure=measure_data["measure"],
                type=measure_data["type"],
                measure_level_id=measure_data["measure_level_id"],
            )
            db.session.add(measure)
            db.session.commit()
            return 200, measure.id, measure
        except Exception as e:
            return make_response(jsonify({'message': 'Error creating measure'}), 500)

    @classmethod
    def get_all_measures(cls):
        try:
            measures = Measure.query.all()
            return measures, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting measures'}), 500)

    @classmethod
    def get_measure_by_id(cls, measure_id):
        try:
            measure = Measure.query.filter_by(id=measure_id).first()
            if not measure:
                return jsonify({'error': 'Measure not found'})
            else:
                return measure, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting measure'}), 500)

    @classmethod
    def update_measure(cls, measure_id, measure_data):
        try:
            measure = Measure.query.filter_by(id=measure_id).first()
            if not measure:
                return jsonify({'error': 'Measure not found'})

            for key, value in measure_data.items():
                setattr(measure, key, value)
            db.session.commit()

            updated_mesure = Measure.query.get(measure_id)
            return updated_mesure, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error updating measure'}), 500)

    @classmethod
    def delete_measure(cls, measure_id):
        try:
            measure = Measure.query.get(measure_id)
            if not measure:
                return jsonify({'error': 'Measure not found'})
            else:
                db.session.delete(measure)
                db.session.commit()
                return {'message': f'Measure with Id {measure_id} deleted successfully'}, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error deleting measure'}), 500)
