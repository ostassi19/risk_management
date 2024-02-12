from models.damage import Damage, db
from flask import make_response, jsonify
from traceback import format_exc


class DamageService:

    @classmethod
    def create_damage(cls, damage_data):
        try:
            damage = Damage(
                security_impact=damage_data["security_impact"],
                consequence_type=damage_data["consequence_type"],
                name=damage_data["name"],
                damage_type=damage_data["damage_type"],
                comment=damage_data["comment"],
                selection=damage_data["selection"],
            )
            print("damage", damage)
            db.session.add(damage)
            db.session.commit()
            return damage
        except Exception as e:
            print(f"Error creating damage: {e}")
            #print(format_exc())  # Print the traceback
            return 500, "Internal server error"

    @classmethod
    def get_all_damages(cls):
        try:
            damage = Damage.query.all()
            return damage, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting damage '}), 500)

    @classmethod
    def get_damage_by_id(cls, damage_id):
        try:
            damage = Damage.query.filter_by(id=damage_id).first()
            if not damage:
                return jsonify({'error': 'damage not found'})
            else:
                return damage, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting damage '}), 500)

    @classmethod
    def update_damage(cls, damage_id, damage_data):
        try:
            damage = Damage.query.filter_by(id=damage_id).first()
            if not damage:
                return jsonify({'error': 'damage not found'})

            for key,value in damage_data.items():
                setattr(damage_data,key,value)

            db.session.commit()

            updated_damage = Damage.query.get(damage_id)
            return updated_damage, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting damage '}), 500)

    @classmethod
    def delete_damage(cls, damage_id):
        try:
            damage = Damage.query.get(damage_id)
            if not damage:
                return jsonify({'error': 'damage not found'})
            else:
                db.session.delete(damage)
                db.session.commit()
                return {'message': {f'Damage with Id {damage_id} deleted successfully'}},200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting damage '}), 500)
