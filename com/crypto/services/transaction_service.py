from com.crypto.repositories.transaction_repo import TransactionRepository


class TransactionService:
    @staticmethod
    def create_transaction(value, sender_id, receiver_id):
        # Business logic like validation goes here
        return TransactionRepository.create_transaction(value, sender_id, receiver_id)

    @staticmethod
    def get_user_transactions(user_id):
        return TransactionRepository.get_transactions_by_user(user_id)
