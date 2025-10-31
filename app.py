from data_management import DataManagement, DataVisualizer

data_manager = DataManagement()

while True:
    choice = data_manager.select_menu()
    if choice == '0':
        data_manager.import_file()
    elif choice == '1':
        data_manager.view_all_transactions()
    elif choice == '2':
        data_manager.view_transactions_by_date_range()
    elif choice == '3':
        data_manager.add_transaction()
    elif choice == '4':
        data_manager.edit_transaction()
    elif choice == '5':
        data_manager.delete_transaction()
    elif choice == '6':
        data_visualizer.analyze_spending_by_category()
    elif choice == '12':
        data_visualizer = DataVisualizer()
        data_visualizer.visualize_monthly_trends()
        data_visualizer.visualize_spending_category()
    elif choice == '13':
        data_manager.save_transactions()
    elif choice == '14':
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please try again.")


