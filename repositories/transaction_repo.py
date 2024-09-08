from com.crypto.models.models import Transaction, db


class TransactionRepository:
    @staticmethod
    def create_transaction(value, sender_id, receiver_id):
        new_transaction = Transaction(value=value, sender_id=sender_id, receiver_id=receiver_id)
        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction

    @staticmethod
    def get_transactions_by_user(user_id):
        return Transaction.query.filter((Transaction.sender_id == user_id) | (Transaction.receiver_id == user_id)).all()
