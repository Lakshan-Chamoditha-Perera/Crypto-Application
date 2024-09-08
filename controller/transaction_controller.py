from flask import Blueprint, request, jsonify
from services.transaction_service import TransactionService
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

transaction_controller = Blueprint('transaction_controller', __name__)

@transaction_controller.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    logger.info(f"Received data for new transaction: {data}")
    
    try:
        transaction = TransactionService.create_transaction(data['value'], data['sender_id'], data['receiver_id'])
        logger.info(f"Transaction created with value: {transaction.value}")
        return jsonify({"message": "Transaction created!", "transaction": {"value": str(transaction.value)}}), 201
    except Exception as e:
        logger.error(f"Error creating transaction: {e}")
        return jsonify({"message": "Transaction creation failed"}), 500

@transaction_controller.route('/transaction/<string:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    logger.info(f"Fetching transaction with ID: {transaction_id}")
    
    transaction = TransactionService.get_transaction(transaction_id)
    if transaction:
        return jsonify({"value": str(transaction['value']), "sender_id": transaction['sender_id'], "receiver_id": transaction['receiver_id']})
    
    logger.warning(f"Transaction with ID {transaction_id} not found")
    return jsonify({"message": "Transaction not found"}), 404

@transaction_controller.route('/transactions', methods=['GET'])
def list_transactions():
    logger.info("Fetching all transactions")
    
    transactions = TransactionService.list_transactions()
    if transactions:
        logger.info(f"Found {len(transactions)} transactions")
    else:
        logger.info("No transactions found")
        
    return jsonify([{"value": str(transaction['value']), "sender_id": transaction['sender_id'], "receiver_id": transaction['receiver_id']} for transaction in transactions])
