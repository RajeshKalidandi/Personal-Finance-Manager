import sys
from services.auth_service import AuthService
from services.transaction_service import TransactionService
from services.report_service import ReportService
from services.budget_service import BudgetService
from services.backup_service import BackupService  # Import the new BackupService

def main():
    print("Welcome to Personal Finance Manager")
    auth_service = AuthService()
    transaction_service = TransactionService()
    report_service = ReportService()
    budget_service = BudgetService()
    backup_service = BackupService("finance.db", "backups")  # Initialize BackupService

    # Main application loop
    while True:
        if not auth_service.is_logged_in():
            choice = input("1. Login\n2. Register\n3. Exit\nChoose an option: ")
            if choice == '1':
                auth_service.login()
            elif choice == '2':
                auth_service.register()
            elif choice == '3':
                sys.exit()
        else:
            choice = input("1. Add Transaction\n2. View Transactions\n3. Generate Report\n4. Manage Budget\n5. Backup Data\n6. Restore Data\n7. Logout\nChoose an option: ")
            if choice == '1':
                transaction_service.add_transaction(auth_service.current_user[0])
            elif choice == '2':
                transaction_service.view_transactions(auth_service.current_user[0])
            elif choice == '3':
                report_service.generate_report(auth_service.current_user[0])
            elif choice == '4':
                budget_service.manage_budget(auth_service.current_user[0])
            elif choice == '5':
                backup_file = backup_service.create_backup()
                print(f"Backup created: {backup_file}")
            elif choice == '6':
                backup_file = input("Enter the backup file name to restore: ")
                try:
                    backup_service.restore_backup(backup_file)
                    print("Backup restored successfully")
                except FileNotFoundError as e:
                    print(str(e))
            elif choice == '7':
                auth_service.logout()

if __name__ == "__main__":
    main()