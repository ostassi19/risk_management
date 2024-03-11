from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request
from services.company_service import CompanyService

company_controller = Namespace('company', description='company entity')

company_model = company_controller.model('company', {
    "id": fields.Integer(readonly=True, description="identifier"),
    "company_name": fields.String(required=True, description="company_name"),
    "company_address": fields.String(required=True, description="company_address"),
})

@company_controller.route('/')
@company_controller.response(500, 'Internal server error')
class CompanyResource(Resource):
    @company_controller.marshal_with(company_model, description="company created successfully")
    @company_controller.expect(company_model)
    @company_controller.response(201, "{'message': 'company registered ")
    @jwt_required()
    def post(self):
        """
        Create a new company.
        """
        company_data = request.json
        return CompanyService.create_company(company_data)

    @company_controller.marshal_list_with(company_model, code=200, description="Success")
    @company_controller.response(200, "{'message': 'success ")
    @company_controller.response(404, "{'message': 'not found ")
    @jwt_required()
    def get(self):
        """
        Get all companys.
        """
        return CompanyService.get_all_companys()

@company_controller.route('/<int:company_id>')
@company_controller.param('company_id', 'the company identifier')
@company_controller.response(500, 'Internal server error')
class CompanyDetailResource(Resource):
    @company_controller.marshal_with(company_model, description="get company by id")
    @company_controller.response(200, 'success')
    @company_controller.response(404, "company not found")
    @jwt_required()
    def get(self, company_id):
        """
        Get details of a specific company.
        """
        company = CompanyService.get_company_by_id(company_id)
        if company:
            return company
        return {"message": "company not found"}, 404

    @company_controller.marshal_with(company_model, description="update company")
    @company_controller.response(404, "company not found")
    @company_controller.response(200, 'success')
    @company_controller.expect(company_model)
    @jwt_required()
    def put(self, company_id):
        """
        Update details of a specific company.
        """
        company_data = request.json
        updated_company = CompanyService.update_damage(company_id, company_data)
        if updated_company:
            return updated_company
        return {"message": "company not found"}, 404

    @company_controller.marshal_with(company_model, code=200, description="Success")
    @company_controller.response(404, "company not found")
    @jwt_required()
    def delete(self, company_id):
        """
        Delete a specific company.
        """
        deleted_company = CompanyService.delete_company(company_id)
        if deleted_company:
            return deleted_company
        return {"message": "company not found"}, 404
