import unittest
from app import app
from unittest.mock import patch

class TestTransactionController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('services.transaction_service.TransactionService.create_transaction')
    def test_create_transaction(self, mock_create_transaction):
        mock_create_transaction.return_value = {'value': 100, 'sender_id': 1, 'receiver_id': 2}

        response = self.app.post('/transaction', json={
            "value": 100,
            "sender_id": 1,
            "receiver_id": 2
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn('Transaction created!', str(response.data))

    @patch('services.transaction_service.TransactionService.get_transaction')
    def test_get_transaction(self, mock_get_transaction):
        mock_get_transaction.return_value = {'value': 100, 'sender_id': 1, 'receiver_id': 2}

        response = self.app.get('/transaction/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('100', str(response.data))

    @patch('services.transaction_service.TransactionService.get_transaction')
    def test_get_transaction_not_found(self, mock_get_transaction):
        mock_get_transaction.return_value = None

        response = self.app.get('/transaction/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Transaction not found', str(response.data))

    @patch('services.transaction_service.TransactionService.list_transactions')
    def test_list_transactions(self, mock_list_transactions):
        mock_list_transactions.return_value = [{'value': 100, 'sender_id': 1, 'receiver_id': 2}]

        response = self.app.get('/transactions')
        self.assertEqual(response.status_code, 200)
        self.assertIn('100', str(response.data))

if __name__ == '__main__':
    unittest.main()
