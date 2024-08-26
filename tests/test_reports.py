import unittest
from services.report_service import ReportService

class TestReportService(unittest.TestCase):
    def setUp(self):
        self.report_service = ReportService()

    def test_generate_report(self):
        # Mock user input and transaction service
        self.report_service.transaction_service.get_transactions_by_period = lambda *args: [
            (1, 1, 1000.0, 'Salary', 'Monthly salary', '2023-05-01', 'income'),
            (2, 1, 100.0, 'Food', 'Groceries', '2023-05-02', 'expense'),
            (3, 1, 200.0, 'Utilities', 'Electricity bill', '2023-05-03', 'expense')
        ]

        # Test generating a report
        self.report_service.generate_report(1)
        self.assertTrue(True)  # If no exception is raised, the test passes

if __name__ == '__main__':
    unittest.main()