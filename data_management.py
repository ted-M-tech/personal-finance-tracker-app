import pandas as pd
import os

class DataManagement:
    def __init__(self, file_name="transactions.csv"):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            self.transactions = pd.read_csv(self.file_name)
            self.transactions = self.transactions.sort_values(by="Date")
            print(f"Loaded transactions from {self.file_name}")
        else:
            self.transactions = pd.DataFrame(columns=["Date", "Description", "Category", "Type", "Amount"])
            print("Initialized empty transactions")

    def select_menu(self):
        print('\n' *2)
        print('=== Personal Finance Tracker ===')
        print('''
 0. Import Financial CSV Data
 1. View All Transactions
 2. View Transactions by Date Range
 3. Add a Transaction
 4. Edit a Transaction
 5. Delete a Transaction
 6. Analyze Spending by Category
 7. Calculate Average Monthly Spending
 8. Show Top Spending Category
 9. Set Monthly Income
 10. Set Category Budget
 11. Check Budget Status
 12. Visualize Spending Trends
 13. Save Transactions to CSV
 14. Exit
                ''')
        print('================================')
        choice = input('Choose an option (0-14): ')
        return choice

    def import_file(self):
        file_path = input(f"Enter the path to the CSV file : ")
        if file_path.endswith('.csv'):
            self.transactions = pd.read_csv(file_path)
            print("CSV file imported successfully.")
            self.file_name = file_path  # update to last used name
        else:
            raise ValueError("Unsupported file format")

    def view_all_transactions(self):
        print("All Transactions:")
        print(self.transactions)

    def save_transactions(self):
        save_filename = input("Enter the filename to save (e.g., 'transaction.csv'): ")

        if file_path.endswith('.csv'):
            self.transactions.to_csv(save_filename, index=False)
            print(f"Transactions saved to {save_filename}")
        else:
            raise ValueError("Unsupported file format")
