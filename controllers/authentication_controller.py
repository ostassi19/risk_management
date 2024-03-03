from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from flask import request
from models.user import User
from services.authentication_service import AuthService

auth_controller = Namespace('auth', description='Authentication')

LOGIN = auth_controller.model('Login', {
    'username': fields.String(required=True, default='test@test.com', description='The user identifier'),
    'password': fields.String(required=True, default='test', description='The user password')
})

LOGIN_SUCCESS = auth_controller.model('Login_success', {
    '_id': fields.String(required=True, description='username'),
    'username': fields.String(required=True, description='username'),
    'last_use': fields.String(required=True, description='last use'),
})


@auth_controller.route('/register')
@auth_controller.response(400, 'Bad Request')
@auth_controller.response(201, 'User registered successfully')
class RegisterResource(Resource):
    @auth_controller.expect(LOGIN)
    def post(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')

        registration_result = AuthService.register_user(username, password)
        return registration_result


@auth_controller.route('/login')
@auth_controller.response(404, 'email or password not correct')
class UserLogin(Resource):
    @auth_controller.response(200, 'Success')
    @auth_controller.expect(LOGIN)
    def post(self):
        """Post email and password to login"""
        return AuthService.login()

@auth_controller.route('/logout')
@auth_controller.response(200, 'Access token revoked')
class UserLogout(Resource):
    @jwt_required()
    def delete(self):
        """Logout"""
        return AuthService.logout()

