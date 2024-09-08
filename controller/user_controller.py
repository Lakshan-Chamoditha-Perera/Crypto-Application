from flask import Blueprint, request, jsonify
from services.user_service import UserService
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    logger.info(f"Received data for new user: {data}")
    
    try:
        user = UserService.create_user(data['email'], data['name'], data['password'])
        logger.info(f"User created with email: {user.email}")
        return jsonify({"message": "User created!", "user": {"email": user.email}}), 201
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return jsonify({"message": "User creation failed"}), 500

@user_controller.route('/user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    logger.info(f"Fetching user with ID: {user_id}")
    
    user = UserService.get_user(user_id)
    if user:
        return jsonify({"email": user['email'], "name": user['name']})
    
    logger.warning(f"User with ID {user_id} not found")
    return jsonify({"message": "User not found"}), 404

@user_controller.route('/users', methods=['GET'])
def list_users():
    logger.info("Fetching all users")
    
    users = UserService.list_users()
    if users:
        logger.info(f"Found {len(users)} users")
    else:
        logger.info("No users found")
        
    return jsonify([{"email": user['email'], "name": user['name']} for user in users])
