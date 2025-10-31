import pandas as pd
import matplotlib.pyplot as plt
import os

class DataManagement:
    def __init__(self, file_name="transactions.csv"):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            self.transactions = pd.read_csv(self.file_name)
            self.transactions = self.transactions.sort_values(by="Date").reset_index(drop=True)
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

    def edit_transaction(self):
        transaction_no = input("Enter the index of the transaction to edit: ")
        if transaction_no.isdigit():
            transaction_no = int(transaction_no)
            if 0 <= transaction_no < len(self.transactions):
                print("\nCurrent Transaction Details:")
                print(  self.transactions.iloc[transaction_no])
                
                new_date = input("\nEnter new date (YYYY-MM-DD) or press Enter to keep current: ")
                new_description = input("Enter new description or press Enter to keep current: ")
                new_category = input("Enter new category or press Enter to keep current: ")
                new_type = input("Enter new type (Income/Expense) or press Enter to keep current: ")
                new_amount = input("Enter new amount or press Enter to keep current: ")

                if new_date:
                    self.transactions.at[transaction_no, 'Date'] = new_date
                if new_description:
                    self.transactions.at[transaction_no, 'Description'] = new_description
                if new_category:
                    self.transactions.at[transaction_no, 'Category'] = new_category
                if new_type:
                    self.transactions.at[transaction_no, 'Type'] = new_type
                if new_amount:
                    self.transactions.at[transaction_no, 'Amount'] = float(new_amount)
                # Save changes
                self.transactions.to_csv(self.file_name, index=False)
                print(f"\nTransaction {transaction_no} updated successfully!")
            else:
                print(f"\nInvalid index.")
        else:
            print("\nInvalid input. Please enter a valid transaction number.")

    def delete_transaction(self):
        transaction_no = input("Enter the transaction number to delete: ")
        if transaction_no.isdigit():
            transaction_no = int(transaction_no)
            if 0 <= transaction_no < len(self.transactions):
                self.transactions = self.transactions.drop(transaction_no).reset_index(drop=True)
                # Save changes
                self.transactions.to_csv(self.file_name, index=False)
                print(f"Transaction {transaction_no} deleted.")
            else:
                print(f"Invalid transaction number: {transaction_no}")
        else:
            print("Invalid input. Please enter a valid transaction number.")

    def save_transactions(self):
        save_filename = input("Enter the filename to save (e.g., 'transaction.csv'): ")

        if save_filename.endswith('.csv'):
            self.transactions.to_csv(save_filename, index=False)
            print(f"Transactions saved to {save_filename}")
        else:
            raise ValueError("Unsupported file format")

class DataVisualizer(DataManagement):
    def __init__(self):
        super().__init__()

    def visualize_spending_category(self):
        plt.figure(figsize=(10, 6))
        category_sums = self.transactions[self.transactions['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
        category_sums.plot(kind='bar', title='Spending by Category')
        plt.xlabel('Category')
        plt.ylabel('Total Spending')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
