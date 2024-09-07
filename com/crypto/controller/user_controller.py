from flask import Blueprint, request, jsonify

from com.crypto.services.user_service import UserService

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['email'], data['name'], data['password'])
    return jsonify({"message": "User created!", "user": {"id": user.id, "email": user.email}}), 201

@user_controller.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user(user_id)
    if user:
        return jsonify({"id": user.id, "email": user.email, "name": user.name})
    return jsonify({"message": "User not found"}), 404

@user_controller.route('/users', methods=['GET'])
def list_users():
    users = UserService.list_users()
    return jsonify([{"id": user.id, "email": user.email, "name": user.name} for user in users])
