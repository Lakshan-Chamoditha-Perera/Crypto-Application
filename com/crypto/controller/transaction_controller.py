from flask import Blueprint, request, jsonify

from com.crypto.services.transaction_service import TransactionService

transaction_controller = Blueprint('transaction_controller', __name__)

@transaction_controller.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction = TransactionService.create_transaction(data['value'], data['sender_id'], data['receiver_id'])
    return jsonify({"message": "Transaction created!", "transaction": {"id": transaction.id, "value": transaction.value}}), 201

@transaction_controller.route('/user/<int:user_id>/transactions', methods=['GET'])
def get_user_transactions(user_id):
    transactions = TransactionService.get_user_transactions(user_id)
    return jsonify([{"id": txn.id, "value": txn.value, "timestamp": txn.timestamp} for txn in transactions])
