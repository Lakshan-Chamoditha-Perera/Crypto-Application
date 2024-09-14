import unittest
from app import app
from unittest.mock import patch

class TestUserController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('services.user_service.UserService.create_user')
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = {'email': 'test@example.com', 'name': 'Test User'}

        response = self.app.post('/user', json={
            "email": "test@example.com",
            "name": "Test User",
            "password": "password123"
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn('User created!', str(response.data))

    @patch('services.user_service.UserService.get_user')
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = {'email': 'test@example.com', 'name': 'Test User'}

        response = self.app.get('/user/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('test@example.com', str(response.data))

    @patch('services.user_service.UserService.get_user')
    def test_get_user_not_found(self, mock_get_user):
        mock_get_user.return_value = None

        response = self.app.get('/user/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', str(response.data))

    @patch('services.user_service.UserService.list_users')
    def test_list_users(self, mock_list_users):
        mock_list_users.return_value = [{'email': 'test@example.com', 'name': 'Test User'}]

        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('test@example.com', str(response.data))

if __name__ == '__main__':
    unittest.main()
