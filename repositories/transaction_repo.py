from models.models import Transaction

class TransactionRepository:
    @staticmethod
    def create_transaction(value, sender_id, receiver_id):
        transaction = Transaction(value=value, sender_id=sender_id, receiver_id=receiver_id)
        transaction.save()
        return transaction

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return Transaction.find_by_id(transaction_id)

    @staticmethod
    def get_all_transactions():
        return Transaction.find_all()
