from models.test import Test, db
from flask import make_response,jsonify

class TestService:
    def post(test):
        try:

            # Assuming 'test_data' is a dictionary with 'name' key

            name = test.get('name')

            # Validate if 'name' is present in the incoming data
            if not name:
                return make_response(jsonify({'error': 'Name is required in the request data'}), 400)
            new_test = Test(name=name)
            print("name: ",name)
            db.session.add(new_test)
            db.session.commit()
            return new_test,200
        except Exception as e:
            return make_response(jsonify({'error from the server side'}),500)

    def get():
        try:
            tests = Test.query.all()
            return tests, 200
        except Exception as e:
            return make_response(jsonify({'error from the server side'}),500)