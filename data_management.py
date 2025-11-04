import pandas as pd
import matplotlib.pyplot as plt
import os

class DataManagement:
    def __init__(self, file_name="transactions.csv"):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            self.transactions = pd.read_csv(self.file_name)
            # Convert all 'Date' column values to datetime to handle data easily
            self.transactions['Date'] = pd.to_datetime(self.transactions['Date'], errors='coerce')
            self.transactions['Amount'] = pd.to_numeric(self.transactions['Amount'], errors='coerce')
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
        print(self.transactions.to_string(index=True))

    def view_transactions_by_date_range(self):    
        start_date_input = input("Enter start date (YYYY-MM-DD): ")
        end_date_input = input("Enter end date (YYYY-MM-DD): ")
        start_date = pd.to_datetime(start_date_input).date()
        end_date = pd.to_datetime(end_date_input).date()
        filtered = self.transactions[
            (self.transactions['Date'].dt.date >= start_date) & (self.transactions['Date'].dt.date <= end_date)
            ]
        print(f"\n--- Transactions from {start_date_input} to {end_date_input} ---")
        print(filtered)
    
    def add_transaction(self):
        date = pd.to_datetime(input("Enter the date (YYYY-MM-DD): "))
        category = input("Enter the category (e.g, Food, Rent): ")
        description = input("Enter a description: ")
        amount = float(input("Enter the amount: "))
        type = int(input("Enter the type number ([1] Income, [2] Expense): "))
        if type == 1:
            type = "Income"
        elif type == 2:
            type = "Expense"
        else:
            raise ValueError("Invalid type. Please enter 1 for Income or 2 for Expense.")


        new_transaction = {
            'Date': date,
            'Category': category,
            'Description': description,
            'Amount': amount,
            'Type': type
        }

        self.transactions = pd.concat(
            [self.transactions, pd.DataFrame([new_transaction])],
            ignore_index=True
        )
        # Save changes
        self.transactions.to_csv(self.file_name, index=False)
        print("Transaction added successfully!")

    def edit_transaction(self):
        transaction_no = input("Enter the index of the transaction to edit: ")
        if transaction_no.isdigit() and 0 <= int(transaction_no) < len(self.transactions):
            print("\nCurrent Transaction Details:")
            print(self.transactions.iloc[int(transaction_no)])

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
            print("\nInvalid input. Please enter a valid transaction number.")
    
    def delete_transaction(self):
        transaction_no = input("Enter the transaction number to delete: ")
        if transaction_no.isdigit() and 0 <= int(transaction_no) < len(self.transactions):
            self.transactions = self.transactions.drop(int(transaction_no)).reset_index(drop=True)
            # Save changes
            self.transactions.to_csv(self.file_name, index=False)
            print(f"Transaction {transaction_no} deleted.")
        else:
            print("Invalid input. Please enter a valid transaction number.")

    def calculate_average_monthly_spending(self):
        expenses = self.transactions[self.transactions['Type'] == 'Expense']
        monthly_spending = expenses.groupby(expenses['Date'].dt.to_period('M'))['Amount'].sum()
        average_monthly_spending = monthly_spending.mean()
        print("\n--- Average Monthly Spending ---")
        print(f"{average_monthly_spending:.2f} (based on {len(monthly_spending)} month(s))")

    def save_transactions(self):
        save_filename = input("Enter the filename to save (e.g., 'transaction.csv'): ")

        if save_filename.endswith('.csv'):
            self.transactions.to_csv(save_filename, index=False)
            print(f"Transactions saved to {save_filename}")
        else:
            raise ValueError("Unsupported file format")

    def analyze_spending_by_category(self):
        category_sums = self.transactions[self.transactions['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
        top_category_sums = category_sums.sort_values(ascending=False)
        print("\n--- Total Spending by Category ---")
        print(top_category_sums)

class DataVisualizer(DataManagement):
    def __init__(self):
        super().__init__()

    def visualize_monthly_trends(self):
        plt.figure(figsize=(10, 6))
        self.transactions['Date'] = pd.to_datetime(self.transactions['Date'])
        self.transactions['Month'] = self.transactions['Date'].dt.strftime('%Y-%m')
        monthly_income = self.transactions[self.transactions['Type'] == 'Income'].groupby('Month')['Amount'].sum()
        monthly_expense = self.transactions[self.transactions['Type'] == 'Expense'].groupby('Month')['Amount'].sum()
        plt.plot(monthly_income.index, monthly_income.values, label='Income', marker='o')
        plt.plot(monthly_expense.index, monthly_expense.values, label='Expense', marker='o')
        plt.xlabel('Month')
        plt.ylabel('Total Amount')
        plt.title('Monthly Income and Expense Trends')
        plt.legend()
        plt.show()

    def visualize_spending_category(self):
        plt.figure(figsize=(10, 6))
        category_sums = self.transactions[self.transactions['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
        category_sums.plot(kind='bar', title='Spending by Category')
        plt.xlabel('Category')
        plt.ylabel('Total Spending')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def visualize_distribution_category(self):
        plt.figure(figsize=(10, 6))
        category_sums = self.transactions.groupby('Category')['Amount'].sum().sort_values(ascending=True)
        plt.title('Distribution of Category')
        plt.pie(category_sums,  autopct='%.0f%%', pctdistance=0.8, startangle=90)
        labels_percentage = [f"{cat}: {percentage:.1f}%" for cat, percentage in zip(category_sums.index, (category_sums / category_sums.sum()) * 100)]
        plt.legend(labels=labels_percentage, title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

class BudgetManager(DataManagement):
    def __init__(self, transactions_file="transactions.csv", budget_file="category_budgets.csv"):
        super().__init__(transactions_file)        
        self.budget_file = budget_file
        if os.path.exists(self.budget_file):
            self.budgets = pd.read_csv(self.file_name)
            print(f"Loaded transactions from {self.file_name}")
        else:
            df_empty = pd.DataFrame(columns=["Category", "Budget"])
            df_empty.to_csv(self.budget_file, index=False)
            print("Initialized empty budgets")

    def set_budgets(self):
        print("\n--- Set budget for a single month and category ---")      
        categories = self.transactions[self.transactions["Type"] != "Income"]["Category"].unique()
        budgets = {}
        for cat in categories:
            while True:
                entry = input(f"Enter your budget for {cat}: ")
                try:
                    budgets[cat] = float(entry)
                    break
                except ValueError:
                    print("Please enter a valid number!")
        self.budgets = budgets
        self.save_budgets()
        print("\nYour budgets have been set:")
        for cat in categories:
            budget = self.budgets[cat]
            print(f"- {cat} : ${budget:.2f}")
        

    def save_budgets(self):
        rows = []
        for cat, budget in self.budgets.items():   
            rows.append({'Category': cat, 'Budget': budget})
        df = pd.DataFrame(rows)
        df.to_csv(self.budget_file, index=False)
        print(f"Budgets saved to {self.budget_file}")
 
    def check_budget_status(self):
        month = str(input("Enter month to check (yyyy-mm): "))
        df_month = self.transactions[self.transactions['Date'].dt.strftime('%Y-%m') == month]
        actual_spending = df_month.groupby("Category")["Amount"].sum().to_dict()
        print("\n----- Budget Status -----")
        alerts_cat = []
        warning_cat = []
        over_count = 0
        categories = list(self.budgets.keys())
        for cat, budget in self.budgets.items():
            budget = self.budgets[cat].get(month, 0)
            spent = actual_spending.get(cat, 0)
            status = f"- {cat}: ${spent:.2f} / ${budget:.2f}"
            if spent > budget:
                status += "   (Alert: Exceeded budget!)"
                alerts_cat.append(cat.lower())
                over_count += 1
            elif spent >= 0.9 * budget:
                status += "   (Warning: Close to budget!)"
                warning_cat.append(cat.lower())
            print(status)
        #Suggestions
        print("\nSuggestions:")
        if over_count == len(categories):
            print("You should review your budgets for all categories.")
        else:
            if alerts_cat:
                print(f"- Consider reducing spending or adjusting the budget for: {', '.join(alerts_cat)}.")
            if warning_cat:
                print(f"- Monitor your spending for: {', '.join(warning_cat)} to avoid exceeding the budget.")
            if not alerts_cat and not warning_cat:
                print("- You are within budget for other categories. Keep up the good work!")
