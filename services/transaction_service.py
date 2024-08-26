from database.db_manager import DatabaseManager
from models.transaction import Transaction
from datetime import datetime

class TransactionService:
    def __init__(self):
        self.db = DatabaseManager()

    def add_transaction(self, user_id):
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description (optional): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        type = input("Enter type (income/expense): ").lower()

        if type not in ['income', 'expense']:
            print("Invalid type. Please enter 'income' or 'expense'.")
            return

        self.db.execute("""
            INSERT INTO transactions (user_id, amount, category, description, date, type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, amount, category, description, date, type))
        self.db.commit()
        print("Transaction added successfully!")

    def view_transactions(self, user_id):
        self.db.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY date DESC", (user_id,))
        transactions = self.db.fetchall()

        if not transactions:
            print("No transactions found.")
            return

        for t in transactions:
            transaction = Transaction(*t)
            print(f"Date: {transaction.date}, Type: {transaction.type}, Amount: {transaction.amount}, Category: {transaction.category}, Description: {transaction.description}")

    def get_transactions_by_period(self, user_id, start_date, end_date):
        self.db.execute("""
            SELECT * FROM transactions 
            WHERE user_id = ? AND date BETWEEN ? AND ?
            ORDER BY date
        """, (user_id, start_date, end_date))
        return [Transaction(*t) for t in self.db.fetchall()]