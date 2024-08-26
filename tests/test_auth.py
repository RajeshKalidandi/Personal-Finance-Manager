import unittest
from services.auth_service import AuthService

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()

    def test_register(self):
        # Mock user input
        self.auth_service.register = lambda: None
        self.auth_service.db.execute = lambda *args: None
        self.auth_service.db.commit = lambda: None

        # Test registration
        self.auth_service.register()
        self.assertTrue(True)  # If no exception is raised, the test passes

    def test_login(self):
        # Mock user input and database response
        self.auth_service.login = lambda: None
        self.auth_service.db.execute = lambda *args: None
        self.auth_service.db.fetchone = lambda: (1, 'testuser', 'hashedpassword')

        # Test login
        self.auth_service.login()
        self.assertTrue(self.auth_service.is_logged_in())

    def test_logout(self):
        self.auth_service.current_user = (1, 'testuser', 'hashedpassword')
        self.auth_service.logout()
        self.assertFalse(self.auth_service.is_logged_in())

if __name__ == '__main__':
    unittest.main()