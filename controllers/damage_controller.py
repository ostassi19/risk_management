from flask_restx import Namespace, Resource, fields
from flask import request
from services.damage_service import DamageService

damage_controller = Namespace('damage', description='Damage entity')

damage_model = damage_controller.model('damage', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "security_impact": fields.String(required=True, description="security impact"),
    "consequence_type": fields.String(required=True, description="consequence type"),
    "name": fields.String(required=True, description="name"),
    "damage_type": fields.String(required=True, description="damage type"),
    "comment": fields.String(required=True, description="comment"),
    "selection": fields.Boolean(required=True, description="selection"),
})

@damage_controller.route('/')
@damage_controller.response(500, 'Internal server error')
class DamageResource(Resource):
    @damage_controller.marshal_with(damage_model, description="Damage created successfully")
    @damage_controller.expect(damage_model)
    @damage_controller.response(201, "{'message': 'damage registered ")
    def post(self):
        """
        Create a new damage.
        """
        damage_data = request.json
        return DamageService.create_damage(damage_data)

    @damage_controller.marshal_list_with(damage_model, code=200, description="Success")
    @damage_controller.response(200, "{'message': 'success ")
    @damage_controller.response(404, "{'message': 'not found ")
    def get(self):
        """
        Get all damages.
        """
        return DamageService.get_all_damages()

@damage_controller.route('/<int:damage_id>')
@damage_controller.param('damage_id', 'the damage identifier')
@damage_controller.response(500, 'Internal server error')
class DamageDetailResource(Resource):
    @damage_controller.marshal_with(damage_model, description="get damage by id")
    @damage_controller.response(200, 'success')
    @damage_controller.response(404, "Damage not found")
    def get(self, damage_id):
        """
        Get details of a specific damage.
        """
        damage = DamageService.get_damage_by_id(damage_id)
        if damage:
            return damage
        return {"message": "Damage not found"}, 404

    @damage_controller.marshal_with(damage_model, description="update damage")
    @damage_controller.response(404, "Damage not found")
    @damage_controller.response(200, 'success')
    @damage_controller.expect(damage_model)
    def put(self, damage_id):
        """
        Update details of a specific damage.
        """
        damage_data = request.json
        updated_damage = DamageService.update_damage(damage_id, damage_data)
        if updated_damage:
            return updated_damage
        return {"message": "Damage not found"}, 404

    @damage_controller.marshal_with(damage_model, code=200, description="Success")
    @damage_controller.response(404, "Damage not found")
    def delete(self, damage_id):
        """
        Delete a specific damage.
        """
        deleted_damage = DamageService.delete_damage(damage_id)
        if deleted_damage:
            return deleted_damage
        return {"message": "Damage not found"}, 404
