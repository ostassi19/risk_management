from models.primary_actif import PrimaryActif, db
from flask import make_response, jsonify

class PrimaryActifService:

    @classmethod
    def create_primary_actif(cls, primary_actif_data):
        try:
            primary_actif = PrimaryActif(
                code=primary_actif_data["code"],
                description=primary_actif_data["description"],
                complementary_description=primary_actif_data["complementary_description"],
                actif_type=primary_actif_data["actif_type"],
                impact_level=primary_actif_data["impact_level"],
            )
            db.session.add(primary_actif)
            db.session.commit()
            return 200, primary_actif
        except Exception as e:
            return make_response(jsonify({'message': 'Error creating Primary Actif'}), 500)

    @classmethod
    def get_all_primary_actifs(cls):
        try:
            primary_actifs = PrimaryActif.query.all()
            return primary_actifs, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Primary Actifs'}), 500)

    @classmethod
    def get_primary_actif_by_id(cls, primary_actif_id):
        try:
            primary_actif = PrimaryActif.query.filter_by(id=primary_actif_id).first()
            if not primary_actif:
                return jsonify({'error': 'Primary Actif not found'})
            else:
                return primary_actif, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Primary Actif'}), 500)

    @classmethod
    def update_primary_actif(cls, primary_actif_id, primary_actif_data):
        try:
            primary_actif = PrimaryActif.query.filter_by(id=primary_actif_id).first()
            if not primary_actif:
                return jsonify({'error': 'Primary Actif not found'})

            for key, value in primary_actif_data.items():
                setattr(primary_actif, key, value)
            db.session.commit()

            updated_primary_actif = PrimaryActif.query.get(primary_actif_id)
            return updated_primary_actif, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error updating Primary Actif'}), 500)

    @classmethod
    def delete_primary_actif(cls, primary_actif_id):
        try:
            primary_actif = PrimaryActif.query.get(primary_actif_id)
            if not primary_actif:
                return jsonify({'error': 'Primary Actif not found'})
            else:
                db.session.delete(primary_actif)
                db.session.commit()
                return {'message': f'Primary Actif with Id {primary_actif_id} deleted successfully'}, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error deleting Primary Actif'}), 500)
