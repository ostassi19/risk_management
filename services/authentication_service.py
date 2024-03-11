from flask import request, jsonify
from flask_jwt_extended import create_access_token, unset_jwt_cookies

from models.user import User, db, hash_password, check_password
from datetime import datetime



class AuthService:
    @staticmethod
    def register_user(user_data):
        username = user_data['username']
        password = user_data['password']
        if not username or not password:
            return {'message': 'Username and password are required'}, 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {'message': 'Username already exists'}, 400

        new_user = User(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            mail=user_data["mail"],
            phone=user_data["phone"],
            address=user_data["address"],
            username=user_data["username"],
            password=hash_password(user_data["password"]),
            last_use = datetime.now(),
            role=user_data["role"],
        )
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

    def login():
        # Récupérer les données de la requête POST
        username = request.json.get('username')
        password = request.json.get('password')
        # Vérifier si l'utilisateur existe dans la base de données
        user = User.query.filter_by(username=username).first()
        if not user or not check_password(user.password, password):
            return jsonify({'message': 'Invalid credentials'}), 401
            # Créer un jeton d'accès pour l'utilisateur
        access_token = create_access_token(identity=user.id)
        # Retourner une réponse JSON avec le jeton d'accès
        response = jsonify({'access_token': access_token})
        return response

    def logout():
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response



