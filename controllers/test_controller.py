from flask_restx import Namespace, Resource,fields
from flask import request
from services.test_service import TestService

test_controller = Namespace('test',description='test entity')

test_model= test_controller.model('test',{
    "id": fields.Integer(readonly= True, description="identifier"),
    "name": fields.String(required = True, descrition=" name of the test")
})

@test_controller.route('/')
class Test(Resource):
    @test_controller.marshal_list_with(test_model)
    @test_controller.response(200,"Success")
    @test_controller.expect(test_model)
    def post(self):
        test= request.json
        return TestService.post(test)

    @test_controller.marshal_list_with(test_model)
    @test_controller.response(200, "Success")
    @test_controller.response(404, "There is no test here")
    def get(self):
        return TestService.get()