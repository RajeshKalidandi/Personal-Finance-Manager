from database.db_manager import DatabaseManager
from services.transaction_service import TransactionService
from datetime import datetime, timedelta

class ReportService:
    def __init__(self):
        self.db = DatabaseManager()
        self.transaction_service = TransactionService()

    def generate_report(self, user_id):
        report_type = input("Enter report type (monthly/yearly): ").lower()
        
        if report_type == 'monthly':
            start_date = datetime.now().replace(day=1).strftime("%Y-%m-%d")
            end_date = (datetime.now().replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            end_date = end_date.strftime("%Y-%m-%d")
        elif report_type == 'yearly':
            start_date = datetime.now().replace(month=1, day=1).strftime("%Y-%m-%d")
            end_date = datetime.now().replace(month=12, day=31).strftime("%Y-%m-%d")
        else:
            print("Invalid report type. Please enter 'monthly' or 'yearly'.")
            return

        transactions = self.transaction_service.get_transactions_by_period(user_id, start_date, end_date)
        
        total_income = sum(t.amount for t in transactions if t.type == 'income')
        total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
        savings = total_income - total_expenses

        print(f"\nFinancial Report ({start_date} to {end_date}):")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Savings: ${savings:.2f}")

        # Category-wise breakdown
        categories = {}
        for t in transactions:
            if t.category not in categories:
                categories[t.category] = {'income': 0, 'expense': 0}
            categories[t.category][t.type] += t.amount

        print("\nCategory-wise Breakdown:")
        for category, amounts in categories.items():
            print(f"{category}:")
            print(f"  Income: ${amounts['income']:.2f}")
            print(f"  Expense: ${amounts['expense']:.2f}")