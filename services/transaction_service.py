from repositories.transaction_repo import TransactionRepository

class TransactionService:
    @staticmethod
    def create_transaction(value, sender_id, receiver_id):
        return TransactionRepository.create_transaction(value, sender_id, receiver_id)

    @staticmethod
    def get_transaction(transaction_id):
        return TransactionRepository.get_transaction_by_id(transaction_id)

    @staticmethod
    def list_transactions():
        return TransactionRepository.get_all_transactions()
