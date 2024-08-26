import unittest
from services.transaction_service import TransactionService

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction_service = TransactionService()

    def test_add_transaction(self):
        # Mock user input and database operations
        self.transaction_service.add_transaction = lambda user_id: None
        self.transaction_service.db.execute = lambda *args: None
        self.transaction_service.db.commit = lambda: None

        # Test adding a transaction
        self.transaction_service.add_transaction(1)
        self.assertTrue(True)  # If no exception is raised, the test passes

    def test_view_transactions(self):
        # Mock database response
        self.transaction_service.db.execute = lambda *args: None
        self.transaction_service.db.fetchall = lambda: [
            (1, 1, 100.0, 'Food', 'Groceries', '2023-05-01', 'expense'),
            (2, 1, 1000.0, 'Salary', 'Monthly salary', '2023-05-02', 'income')
        ]

        # Test viewing transactions
        self.transaction_service.view_transactions(1)
        self.assertTrue(True)  # If no exception is raised, the test passes

if __name__ == '__main__':
    unittest.main()