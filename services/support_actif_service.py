from models.support_actif import SupportActif, db
from flask import make_response, jsonify

class SupportActifService:

    @classmethod
    def create_support_actif(cls, support_actif_data):
        try:
            support_actif = SupportActif(
                name=support_actif_data["name"],
                type=support_actif_data["type"],
                element=support_actif_data["element"],
                selection=support_actif_data["selection"],
            )
            db.session.add(support_actif)
            db.session.commit()
            return 200, support_actif
        except Exception as e:
            return make_response(jsonify({'message': 'Error creating Support Actif'}), 500)

    @classmethod
    def get_all_support_actifs(cls):
        try:
            support_actifs = SupportActif.query.all()
            return support_actifs, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Support Actifs'}), 500)

    @classmethod
    def get_support_actif_by_id(cls, support_actif_id):
        try:
            support_actif = SupportActif.query.filter_by(id=support_actif_id).first()
            if not support_actif:
                return jsonify({'error': 'Support Actif not found'})
            else:
                return support_actif, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error getting Support Actif'}), 500)

    @classmethod
    def update_support_actif(cls, support_actif_id, support_actif_data):
        try:
            support_actif = SupportActif.query.filter_by(id=support_actif_id).first()
            if not support_actif:
                return jsonify({'error': 'Support Actif not found'})

            for key, value in support_actif_data.items():
                setattr(support_actif, key, value)
            db.session.commit()

            updated_support_actif = SupportActif.query.get(support_actif_id)
            return updated_support_actif, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error updating Support Actif'}), 500)

    @classmethod
    def delete_support_actif(cls, support_actif_id):
        try:
            support_actif = SupportActif.query.get(support_actif_id)
            if not support_actif:
                return jsonify({'error': 'Support Actif not found'})
            else:
                db.session.delete(support_actif)
                db.session.commit()
                return {'message': f'Support Actif with Id {support_actif_id} deleted successfully'}, 200
        except Exception as e:
            return make_response(jsonify({'message': 'Error deleting Support Actif'}), 500)
