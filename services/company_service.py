from models.company import Company, db
from flask import make_response, jsonify
from traceback import format_exc


class CompanyService:

    @classmethod
    def create_company(cls, company_data):
        try:
            company = Company(
                company_name=company_data["company_name"],
                company_address=company_data["company_address"],
            )
            db.session.add(company)
            db.session.commit()
            return company
        except Exception as e:
            print(f"Error creating company: {e}")
            #print(format_exc())  # Print the traceback
            return 500, "Internal server error"

    @classmethod
    def get_all_companys(cls):
        try:
            company = Company.query.all()
            return company, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting company '}), 500)

    @classmethod
    def get_company_by_id(cls, company_id):
        try:
            company = Company.query.filter_by(id=company_id).first()
            if not company:
                return jsonify({'error': 'company not found'})
            else:
                return company, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting company '}), 500)

    @classmethod
    def update_company(cls, company_id, company_data):
        try:
            company = Company.query.filter_by(id=company_id).first()
            if not company:
                return jsonify({'error': 'company not found'})

            for key,value in company_data.items():
                setattr(company_data,key,value)

            db.session.commit()

            updated_company = Company.query.get(company_id)
            return updated_company, 200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting company '}), 500)

    @classmethod
    def delete_company(cls, company_id):
        try:
            company = Company.query.get(company_id)
            if not company:
                return jsonify({'error': 'company not found'})
            else:
                db.session.delete(company)
                db.session.commit()
                return {'message': {f'company with Id {company_id} deleted successfully'}},200
        except Exception as e:
            return make_response(jsonify({'message': 'error getting company '}), 500)
