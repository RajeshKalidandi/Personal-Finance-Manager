# Personal Finance Management Application User Manual

## Table of Contents
1. Introduction
2. Installation
3. Getting Started
4. Features
   4.1 User Registration and Authentication
   4.2 Income and Expense Tracking
   4.3 Financial Reports
   4.4 Budgeting
   4.5 Data Backup and Restore
5. Troubleshooting
6. Contact Information

## 1. Introduction

Welcome to the Personal Finance Management Application! This command-line tool helps you manage your personal finances by tracking income, expenses, and generating financial reports. It also includes budgeting features to help you stay on top of your financial goals and a backup system to keep your data safe.

## 2. Installation

To install the Personal Finance Management Application, follow these steps:

1. Ensure you have Python 3.7 or higher installed on your system.
2. Download the application files from the provided source.
3. Open a terminal or command prompt and navigate to the application directory.
4. Install the required dependencies !



## 3. Getting Started

To start the application, run the following command in the terminal:

python main.py 

You will be presented with a menu to either login, register, or exit the application.

## 4. Features

### 4.1 User Registration and Authentication

- To register, choose the "Register" option and follow the prompts to create a username and password.
- To login, choose the "Login" option and enter your credentials.
- You can logout at any time by selecting the "Logout" option from the main menu.


### 4.2 Income and Expense Tracking

- To add a new transaction, select "Add Transaction" from the main menu.
- Enter the required information:
  - Amount
  - Category
  - Description (optional)
  - Type (income or expense)
- To view your transactions, select "View Transactions" from the main menu.

### 4.3 Financial Reports

- To generate a financial report, select "Generate Report" from the main menu.
- Choose between a monthly or yearly report.
- The report will display:
  - Total income
  - Total expenses
  - Savings
  - Category-wise breakdown of income and expenses

### 4.4 Budgeting

- To manage your budget, select "Manage Budget" from the main menu.
- You can:
  - Set a budget for a specific category
  - View your current budgets
  - Check your budget limits
  
### 4.5 Data Backup and Restore

- To create a backup of your data, select "Backup Data" from the main menu.
  - The application will create a backup file and display its name.
  - Backup files are stored in the 'backups' directory.

- To restore data from a backup:
  1. Select "Restore Data" from the main menu.
  2. Enter the name of the backup file when prompted.
  3. The application will restore your data from the specified backup.

It's recommended to create regular backups to prevent data loss.

## 5. Troubleshooting

If you encounter any issues while using the application:

1. Ensure you're using the correct username and password for login.
2. Check that you've entered valid numerical values for transaction amounts and budgets.
3. If the application crashes, restart it and try again.
4. For backup and restore issues:
   - Ensure you have the necessary permissions to read/write in the application directory.
   - Double-check the backup file name when restoring data.
5. If problems persist, please contact our support team.

## 6. Contact Information

For additional support or to report issues, please contact our support team at support@personalfinanceapp.com.

Thank you for using the Personal Finance Management Application!
