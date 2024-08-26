from database.db_manager import DatabaseManager

class BudgetService:
    def __init__(self):
        self.db = DatabaseManager()

    def set_budget(self, user_id):
        category = input("Enter budget category: ")
        amount = float(input("Enter budget amount: "))

        self.db.execute("""
            INSERT OR REPLACE INTO budgets (user_id, category, amount)
            VALUES (?, ?, ?)
        """, (user_id, category, amount))
        self.db.commit()
        print(f"Budget for {category} set to ${amount:.2f}")

    def get_budgets(self, user_id):
        self.db.execute("SELECT category, amount FROM budgets WHERE user_id = ?", (user_id,))
        budgets = self.db.fetchall()

        if not budgets:
            print("No budgets set.")
            return

        print("Current Budgets:")
        for category, amount in budgets:
            print(f"{category}: ${amount:.2f}")

    def check_budget_limits(self, user_id):
        self.db.execute("""
            SELECT b.category, b.amount, COALESCE(SUM(t.amount), 0) as spent
            FROM budgets b
            LEFT JOIN transactions t ON b.user_id = t.user_id AND b.category = t.category
            WHERE b.user_id = ? AND t.type = 'expense' AND strftime('%Y-%m', t.date) = strftime('%Y-%m', 'now')
            GROUP BY b.category
        """, (user_id,))
        
        budget_status = self.db.fetchall()

        for category, budget_amount, spent in budget_status:
            if spent > budget_amount:
                print(f"Warning: You've exceeded your budget for {category}. Budget: ${budget_amount:.2f}, Spent: ${spent:.2f}")
            elif spent > 0.8 * budget_amount:
                print(f"Alert: You're close to exceeding your budget for {category}. Budget: ${budget_amount:.2f}, Spent: ${spent:.2f}")

    def manage_budget(self, user_id):
        while True:
            choice = input("1. Set Budget\n2. View Budgets\n3. Check Budget Limits\n4. Back to Main Menu\nChoose an option: ")
            if choice == '1':
                self.set_budget(user_id)
            elif choice == '2':
                self.get_budgets(user_id)
            elif choice == '3':
                self.check_budget_limits(user_id)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")